from settings import get_price

class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def total(self):
        return get_price(self.product) * self.quantity