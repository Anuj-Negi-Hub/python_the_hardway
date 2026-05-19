# Level 2: Intermediate JSON Handling - Modifying and Saving
# Goal: Read a list of products, apply a discount, and save it to a new JSON file.

import json

input_file = "level2_data.json"
output_file = "level2_discounted.json"

try:
    # 1. Read the JSON file
    with open(input_file, 'r') as file:
        products = json.load(file)     #remember this: convert json data into python object
        print(f"Successfully loaded {len(products)} products.\n")

    # 2. Modify the data (Apply a 10% discount to all items)
    for product in products:
        discount_amount = product['price'] * 0.10
        product['price'] = round(product['price'] - discount_amount, 2)
        
        # Add a new key to show it was discounted
        product['on_sale'] = True
        print(f"Updated {product['name']}: New price is ${product['price']}")

    # 3. Save the modified data back to a new JSON file
    with open(output_file, 'w') as file:
        # json.dump() writes a Python object (dictionary/list) to a file in JSON format
        # indent=4 makes the output file readable and neatly formatted
        json.dump(products, file, indent=4)
        print(f"\nSaved updated products to {output_file}")

except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except json.JSONDecodeError:
    print("Error: The file contains invalid JSON data.")
