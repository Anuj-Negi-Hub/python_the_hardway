class Book():
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show_title(self):
        print(self.title)
    
    def show_price(self):
        print(self.price)



books = []

book_data = [
    ("Python Basics", 299),
    ("Data Science", 499),
    ("AI Guide", 699)
]


# Create objects
for title, price in book_data:
    books.append(Book(title, price))

# Use methods
for book in books:
    book.show_title()
    book.show_price()
    print()
