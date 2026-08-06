'''
Create a program that takes a product name as input and retrieves the current price and quantity for that product.
The product data is in a data file in the JSON format and looks like this:
{
"products" : [
{"name": "Widget", "price": 25.00, "quantity": 5 },
{"name": "Thing", "price": 15.00, "quantity": 5 },
{"name": "Doodad", "price": 5.00, "quantity": 10 }
]
}

Print out the product name, price, and quantity if the product is found.
If no product matches the search, state that no product was found and start over.

Example Output
What is the product name? iPad
Sorry, that product was not found in our inventory.
What is the product name? Widget
Name: Widget
Price: $25.00
Quantity on hand: 5
'''
import json

product_name = input("What is the product name? ")
with open("ex44_product_data.json", "r") as file:
    file_data = json.load(file)

    found = False
    # print(file_data)
    for product in file_data['products']:
        if product_name == product["name"].lower():
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']}")
            print(f"Quantity on hand: {product['quantity']}")
            found = True
            break
        
    # Execute when their is no item with the searched name
    if not found:
        print("Sorry, that product was not found in our inventory.")
