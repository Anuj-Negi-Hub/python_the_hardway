import sqlite3
from datetime import datetime


# =====================================================================
# 1. THE 4 DOMAIN OBJECTS
# =====================================================================

class Customer:
    """Represents a registered user in the system."""
    def __init__(self, name: str, email: str, customer_id: int = None):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name='{self.name}')"


class Product:
    """Represents an item in the store inventory."""
    def __init__(self, name: str, price: float, stock: int, product_id: int = None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price=${self.price}, stock={self.stock})"


class Order:
    """Represents an order header placed by a Customer."""
    def __init__(self, customer_id: int, status: str = "PENDING", 
                 order_date: str = None, order_id: int = None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = status
        self.items = []  # List of OrderItem objects belonging to this order

    def __repr__(self):
        return f"Order(id={self.order_id}, customer_id={self.customer_id}, status='{self.status}')"


class OrderItem:
    """
    Bridge entity resolving the Many-to-Many relationship between Order and Product.
    Captures the exact quantity and unit price at the time of purchase.
    """
    def __init__(self, order_id: int, product_id: int, quantity: int, 
                 unit_price: float, item_id: int = None):
        self.item_id = item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    def __repr__(self):
        return (f"OrderItem(id={self.item_id}, order_id={self.order_id}, "
                f"product_id={self.product_id}, qty={self.quantity}, unit_price=${self.unit_price})")


# =====================================================================
# 2. THE DATABASE MANAGER
# =====================================================================

class StoreDatabase:
    """Handles schema creation, relationships, and multi-object operations."""

    def __init__(self, db_name="ecommerce.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # 1. ALWAYS turn on foreign key constraint checking in SQLite
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()

    def _create_tables(self):
        """Creates tables for all 4 entities with relational constraints."""
        
        # Table 1: Customers
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        # Table 2: Products
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                stock INTEGER NOT NULL CHECK(stock >= 0)
            )
        """)

        # Table 3: Orders (1 Customer -> Many Orders)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'PENDING',
                FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
            )
        """)

        # Table 4: OrderItems (Bridge Table: Links Orders & Products)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                unit_price REAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
                FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
            )
        """)
        self.conn.commit()

    # --- CUSTOMER & PRODUCT HELPERS ---

    def add_customer(self, customer: Customer) -> Customer:
        """Inserts customer and updates customer_id."""
        query = "INSERT INTO customers (name, email) VALUES (?, ?)"
        self.cursor.execute(query, (customer.name, customer.email))
        self.conn.commit()
        customer.customer_id = self.cursor.lastrowid
        return customer

    def add_product(self, product: Product) -> Product:
        """Inserts product and updates product_id."""
        query = "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)"
        self.cursor.execute(query, (product.name, product.price, product.stock))
        self.conn.commit()
        product.product_id = self.cursor.lastrowid
        return product

    # --- MULTI-OBJECT TRANSACTION: CREATING AN ORDER ---

    def create_order(self, customer: Customer, cart_items: list[tuple[Product, int]]) -> Order:
        """
        Coordinates Customer, Order, OrderItem, and Product objects inside a single transaction:
        1. Validates stock for each Product.
        2. Creates the Order record.
        3. Creates OrderItem records for each product in the cart.
        4. Decrements stock on Product records.
        """
        if not customer.customer_id:
            raise ValueError("Customer must be saved in the database before ordering.")

        try:
            # Step A: Validate stock for all items first
            for product, quantity in cart_items:
                if product.stock < quantity:
                    raise ValueError(f"Insufficient stock for '{product.name}' (Available: {product.stock}, Requested: {quantity})")

            # Step B: Insert the Order header
            order = Order(customer_id=customer.customer_id, status="COMPLETED")
            self.cursor.execute(
                "INSERT INTO orders (customer_id, order_date, status) VALUES (?, ?, ?)",
                (order.customer_id, order.order_date, order.status)
            )
            order.order_id = self.cursor.lastrowid

            # Step C: Insert each OrderItem & reduce Product stock in DB
            for product, quantity in cart_items:
                # 1. Insert order item snapshot (lock in price at time of purchase)
                order_item = OrderItem(
                    order_id=order.order_id,
                    product_id=product.product_id,
                    quantity=quantity,
                    unit_price=product.price
                )
                self.cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
                    (order_item.order_id, order_item.product_id, order_item.quantity, order_item.unit_price)
                )
                order_item.item_id = self.cursor.lastrowid
                order.items.append(order_item)

                # 2. Update product stock in database
                self.cursor.execute(
                    "UPDATE products SET stock = stock - ? WHERE id = ?",
                    (quantity, product.product_id)
                )
                # 3. Update the in-memory python product object stock
                product.stock -= quantity

            # Commit entire atomic transaction
            self.conn.commit()
            print(f"✅ Order #{order.order_id} placed successfully for {customer.name}!")
            return order

        except Exception as e:
            self.conn.rollback()  # If anything fails, revert everything
            print(f"❌ Transaction rolled back due to error: {e}")
            raise e

    # --- RELATIONAL QUERY: JOINING ALL 4 TABLES ---

    def print_customer_invoices(self, customer: Customer):
        """
        Demonstrates a multi-table SQL JOIN combining all 4 entities:
        customers -> orders -> order_items -> products
        """
        query = """
            SELECT 
                o.id AS order_id,
                o.order_date,
                o.status,
                p.name AS product_name,
                oi.quantity,
                oi.unit_price,
                (oi.quantity * oi.unit_price) AS line_total
            FROM orders o
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
            WHERE o.customer_id = ?
            ORDER BY o.id, oi.id
        """
        self.cursor.execute(query, (customer.customer_id,))
        rows = self.cursor.fetchall()

        if not rows:
            print(f"\nNo orders found for {customer.name}.")
            return

        print(f"\n=======================================================")
        print(f" INVOICE FOR: {customer.name} ({customer.email})")
        print(f"=======================================================")

        current_order_id = None
        order_total = 0

        for row in rows:
            order_id, order_date, status, product_name, qty, unit_price, line_total = row
            
            # Print new header when order_id changes
            if order_id != current_order_id:
                if current_order_id is not None:
                    print(f"   -> ORDER TOTAL: ${order_total:.2f}\n")
                current_order_id = order_id
                order_total = 0
                print(f"📦 Order #{order_id} | Date: {order_date} | Status: {status}")

            print(f"   - {product_name:<18} | Qty: {qty:<2} | Price: ${unit_price:<7.2f} | Subtotal: ${line_total:.2f}")
            order_total += line_total

        print(f"   -> ORDER TOTAL: ${order_total:.2f}")
        print(f"=======================================================\n")

    def close(self):
        self.conn.close()


# =====================================================================
# 3. INTERACTIVE SIMULATION / DEMONSTRATION
# =====================================================================

if __name__ == "__main__":
    # Remove old DB for fresh run
    import os
    if os.path.exists("ecommerce.db"):
        os.remove("ecommerce.db")

    db = StoreDatabase("ecommerce.db")

    # 1. Create Customers
    alice = Customer("Alice Smith", "alice@example.com")
    bob = Customer("Bob Jones", "bob@example.com")
    db.add_customer(alice)
    db.add_customer(bob)

    # 2. Create Products in Catalog
    laptop = Product("MacBook Air", 999.99, stock=5)
    mouse = Product("Wireless Mouse", 29.99, stock=20)
    monitor = Product("4K Monitor", 399.00, stock=8)
    db.add_product(laptop)
    db.add_product(mouse)
    db.add_product(monitor)

    print("\n--- Initial Inventory ---")
    print(laptop)
    print(mouse)
    print(monitor)

    # 3. Alice places an Order with multiple products
    # Cart: 1 Laptop + 2 Wireless Mice
    print("\n--- Placing Order 1 (Alice) ---")
    alice_cart = [
        (laptop, 1),
        (mouse, 2)
    ]
    order1 = db.create_order(customer=alice, cart_items=alice_cart)

    # 4. Bob places an Order
    # Cart: 1 4K Monitor + 1 Wireless Mouse
    print("\n--- Placing Order 2 (Bob) ---")
    bob_cart = [
        (monitor, 1),
        (mouse, 1)
    ]
    order2 = db.create_order(customer=bob, cart_items=bob_cart)

    # 5. Alice places a SECOND Order
    # Cart: 1 4K Monitor
    print("\n--- Placing Order 3 (Alice again) ---")
    alice_cart_2 = [
        (monitor, 1)
    ]
    order3 = db.create_order(customer=alice, cart_items=alice_cart_2)

    # 6. Check Inventory after purchases (notice stock decreased!)
    print("\n--- Inventory After Orders ---")
    print(laptop)
    print(mouse)
    print(monitor)

    # 7. Print Alice's full invoice summary joining all 4 tables
    db.print_customer_invoices(alice)

    # 8. Test Foreign Key Cascade: Deleting Bob deletes his orders and items automatically
    print("--- Demonstrating Foreign Key ON DELETE CASCADE ---")
    db.cursor.execute("DELETE FROM customers WHERE id = ?", (bob.customer_id,))
    db.conn.commit()
    
    # Check if Bob's orders still exist
    db.cursor.execute("SELECT COUNT(*) FROM orders WHERE customer_id = ?", (bob.customer_id,))
    remaining_orders = db.cursor.fetchone()[0]
    print(f"Deleted Bob. Remaining orders for Bob in database: {remaining_orders} (Automatically cleaned up!)")

    db.close()
