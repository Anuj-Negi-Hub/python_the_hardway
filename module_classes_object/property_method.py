class OrderItem:
    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = quantity * unit_price   # ❌ Set only once at start!

item = OrderItem(quantity=2, unit_price=10)
print(item.subtotal)  # Output: 20

# Now the user changes the quantity to 5:
item.quantity = 5

print(item.subtotal)  # ❌ Output is STILL 20! It did not update!

item = OrderItem(quantity=5, unit_price=10)
print(item.subtotal)
