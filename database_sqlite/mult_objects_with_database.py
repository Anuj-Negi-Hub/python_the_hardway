import sqlite3


# -------------------------------------------------------------
# 1. THE OBJECT MODELS
# -------------------------------------------------------------
class Customer:
    """Represents a Customer object."""
    def __init__(self, name, email, customer_id=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer(ID={self.customer_id}, Name='{self.name}')"


class Order:
    """Represents an Order object linked to a Customer."""
    def __init__(self, customer_id, item_name, amount, order_id=None):
        self.order_id = order_id
        self.customer_id = customer_id  # Foreign Key linking to Customer
        self.item_name = item_name
        self.amount = amount

    def __repr__(self):
        return f"Order(ID={self.order_id}, CustomerID={self.customer_id}, Item='{self.item_name}', Amount=${self.amount})"


# -------------------------------------------------------------
# 2. THE DATABASE MANAGER (Handles Multiple Objects & Relational Queries)
# -------------------------------------------------------------
class ShopDatabase:
    """Manages database tables and relations for Customer and Order objects."""

    def __init__(self, db_name="shop.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # Enable Foreign Key constraints in SQLite
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()

    def _create_tables(self):
        # Create Customers table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        
        # Create Orders table with Foreign Key linking to customers(id)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                item_name TEXT NOT NULL,
                amount REAL NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    # --- CUSTOMER OPERATIONS ---
    def add_customer(self, customer: Customer):
        """Inserts a Customer object into database."""
        query = "INSERT INTO customers (name, email) VALUES (?, ?)"
        self.cursor.execute(query, (customer.name, customer.email))
        self.conn.commit()
        customer.customer_id = self.cursor.lastrowid
        print(f"✅ Added {customer}")

    # --- ORDER OPERATIONS ---
    def place_order(self, customer: Customer, item_name, amount):
        """Creates an Order object linked to the given Customer object."""
        if customer.customer_id is None:
            print("❌ Cannot place order: Customer is not saved in DB yet!")
            return None

        # Create Order object using customer.customer_id
        order = Order(customer_id=customer.customer_id, item_name=item_name, amount=amount)
        
        query = "INSERT INTO orders (customer_id, item_name, amount) VALUES (?, ?, ?)"
        self.cursor.execute(query, (order.customer_id, order.item_name, order.amount))
        self.conn.commit()
        order.order_id = self.cursor.lastrowid
        print(f"🛒 Placed {order}")
        return order

    # --- RELATIONAL QUERY (Fetch all orders for a customer) ---
    def get_orders_for_customer(self, customer: Customer):
        """Returns a list of Order objects belonging to a Customer."""
        query = "SELECT id, customer_id, item_name, amount FROM orders WHERE customer_id = ?"
        self.cursor.execute(query, (customer.customer_id,))
        rows = self.cursor.fetchall()
        
        # Convert DB rows to Order objects
        orders = [Order(order_id=r[0], customer_id=r[1], item_name=r[2], amount=r[3]) for r in rows]
        return orders

    def close(self):
        self.conn.close()


# -------------------------------------------------------------
# 3. HOW MULTIPLE OBJECTS INTERACT WITH DB
# -------------------------------------------------------------
if __name__ == "__main__":
    db = ShopDatabase("shop.db")

    # STEP 1: Create 2 Customer Objects
    c1 = Customer("Alice", "alice@email.com")
    c2 = Customer("Bob", "bob@email.com")

    db.add_customer(c1)  # c1 gets ID = 1
    db.add_customer(c2)  # c2 gets ID = 2

    print("\n--- Placing Orders ---")
    # STEP 2: Place multiple orders for Alice (c1)
    db.place_order(c1, "Laptop", 1200.0)
    db.place_order(c1, "Mouse", 25.0)

    # Place an order for Bob (c2)
    db.place_order(c2, "Headphones", 150.0)

    # STEP 3: Retrieve all Order objects for Alice (c1)
    print(f"\n--- Fetching Orders for {c1.name} ---")
    alice_orders = db.get_orders_for_customer(c1)
    
    total_spent = 0
    for order in alice_orders:
        print(f"  - Item: {order.item_name} (${order.amount})")
        total_spent += order.amount
        
    print(f"Total spent by {c1.name}: ${total_spent}")

    db.close()