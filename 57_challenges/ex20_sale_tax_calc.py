'''
Create a tax calculator that handles multiple states and multiple counties within each state.
The program prompts the user for the order amount and the state where the order will be shipped.

For Wisconsin residents, prompt for the county of residence.
• For Eau Claire county residents, add an additional 0.005 tax.
• For Dunn county residents, add an additional 0.004 tax.

Illinois residents must be charged 8% sales tax with no additional county-level charge.
All other states are not charged tax. The program then displays the tax and the total for Wisconsin and Illinois residents but just the total for everyone else.

Example Output
What is the order amount? 10
What state do you live in? Wisconsin
The tax is $0.50.
The total is $10.50.
'''

ord_amt = float(input("What is the order amount: "))
ord_place = input("In which state have you placed the order: ")

#if the order place is wisconsin
if ord_place == "Wisconsin" or ord_place == "wisconsin":
    county_place = input("Type the county of residency: ")
    if county_place == "Eau Claire" or county_place == "eau claire":
        #formula to calculate tax
        tax = (ord_amt * (5 + 0.005) / 100)
        print(f"That tax is {tax}.")
        total_amt = ord_amt + tax
        print(f"The total amount paid including tax is {total_amt}")
    elif county_place == "Dunn" or county_place == "dunn":
        #formula to calculate tax
        tax = (ord_amt * (5 + 0.004) / 100)
        print(f"That tax is {tax}.")
        total_amt = ord_amt + tax
        print(f"The total amount paid including tax is {total_amt}")

# if the order place is Illinois
elif ord_place == "Illinois" or ord_place == "illinois":
    #formula to calculate tax
    tax = ord_amt * 8 / 100
    print(f"That tax is {tax}.")
    total_amt = ord_amt + tax
    print(f"The total amount paid including tax is {total_amt}")

#for all other states, there is no tax. So the ord_amt becomes the total paid amount.
else:
    print(f"The total amount paid including tax is {ord_amt}")