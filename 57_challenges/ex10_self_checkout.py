'''
Create a simple self-checkout system. Prompt for the prices and quantities of three items.
Calculate the subtotal of the items. Then calculate the tax using a tax rate of 5.5%.
Print out the line items with the quantity and total, and then print out the subtotal, tax amount, and total.

Example Output:
Enter the price of item 1: 25
Enter the quantity of item 1: 2
Enter the price of item 2: 10
Enter the quantity of item 2: 1
Enter the price of item 3: 4
Enter the quantity of item 3: 1
Subtotal: $64.00
Tax: $3.52
Total: $67.52
'''

item_one_price = int(input("Enter the price of the item 1: "))
item_one_quant = int(input("Enter the quantity of the item 1: "))

item_two_price = int(input("Enter the price of the item 2: "))
item_two_quant = int(input("Enter the quantity of the item 2: "))

item_three_price = int(input("Enter the price of the item 3: "))
item_three_quant = int(input("Enter the quantity of the item 3: "))

total_quant = item_one_quant + item_two_quant + item_three_quant
total_price = (item_one_price * item_one_quant) + (item_two_price * item_two_quant) + (item_three_price * item_three_quant)

print(f"The total price of the all items without tax is: {total_price}")
print(f"The total quantity of all the items is: {total_quant}")
tax_rate = 5.5

total_tax = (total_price * 5.5)/100
print(f"The total tax on all the items is: {total_tax}.")
total_with_tax = total_price + total_tax

print(f"the total price of all the items including tax is: {total_with_tax}.")