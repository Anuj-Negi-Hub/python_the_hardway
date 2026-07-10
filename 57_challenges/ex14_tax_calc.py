'''
Write a simple program to compute the tax on an order amount. 
The program should prompt for the order amount and the state. 
If the state is “WI,” then the order must be charged 5.5% tax.
The program should display the subtotal, tax, and total for Wisconsin residents but display just the total for non-residents.

Example Output
What is the order amount? 10
What is the state? WI
The subtotal is $10.00.
The tax is $0.55.
The total is $10.55.
Or
What is the order amount? 10
What is the state? MN
The total is $10.00
'''

ord_amt = float(input("Type the order amount: "))
state_status = input("Type your state name, for example: WI for Wisconsin: ")

tax_per = 5.5
total_tax = ord_amt * tax_per / 100
total_amt = ord_amt + total_tax

if state_status == "WI":
    print(f"The subtotal is {ord_amt}.")
    print(f"The tax is {tax_per}%.")
    print(f"The total is {total_amt}.")
else:
    print(f"The total is {total_amt}.")

#-------------------------------------------------------------------------------------------------------------
#create the same program using function
 
def tax_calc():
    tax_per = 5.5
    total_tax = ord_amt * tax_per / 100
    total_amt = ord_amt + total_tax

    if state_status == "WI":
        print(f"The subtotal is {ord_amt}.")
        print(f"The tax is {tax_per}%.")
        print(f"The total is {total_amt}.")
    else:
        print(f"The total is {total_amt}.")

ord_amt = float(input("Type the order amount: "))
state_status = input("Type your state name, for example: WI for Wisconsin: ")
tax_calc()

