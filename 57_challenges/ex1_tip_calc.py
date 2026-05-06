def calc_tip(bill, tiprte):
    """Calculate the tip value and total amount.
    Need to print the total amount and tip"""
    tip_val = (bill * tiprte) / 100
    tot_amt = bill + tip_val

    # print(f"This is my tip amount {tip_val}.")
    # print(f"The total amount of the bill is {tot_amt}.")
    return [tot_amt, tip_val]

class Bill:
    def __init__(self, bill, tip_rate):
        self.bill_amnt = bill
        self.tip = tip_rate
        self.tot_amt = None
        # self.name = cust_name

    def calc_tip(self, cust_name,):
        self.name = cust_name
        tot_amt = self.tot_amt
        """Calculate the tip value and total amount.
        Need to print the total amount and tip"""
        tip_val = (self.bill_amnt * self.tip) / 100
        tot_amt = self.bill_amnt + tip_val
        self.tot_amt = tot_amt
        print(f"The customer name: {self.name}.")
        print(f"The percentage of the tip on bill amount is {self.tip}.")
        print(f"This is my tip amount {tip_val}.")
        print(f"The total amount of the bill is {tot_amt}.")
    
    def parcel_food(self):
        if self.tot_amt < 1500:
            print("You can take the parcel also.")
        else:
            print("You cannot take the parcel.")

    
#Pass the parameter values using the input functions
bill = int(input("Type the bill amount: "))
tip_rate = int(input("Type the percentag of the tip on bill amount: "))
cust_name = input("Type the customer name: ")


bill1 = Bill(bill, tip_rate)
bill2 = Bill(bill, tip_rate)

bill1.calc_tip(cust_name)
bill2.calc_tip(cust_name)
bill1.parcel_food()
print()

if __name__ == "__main__":
    pass
    # The program should prompt for a bill amount and a tip rate. 
    # bill_amount = int(input("Enter the bill amount: "))
    # tip_rate = int(input("Enter the tip rate in percentage: "))
    # cust_name = input("Enter the customer name: ")
    
    # # The program must compute the tip 
    # tip = (bill_amount * tip_rate)/100

    # # and then display both the tip and the total amount of the bill.
    # print(f"This is my tip amount {tip}.")

    # total_amount = bill_amount + tip
    # print(f"The total amount of the bill is {total_amount}.")

    # calc_tot_aomunt = calc_tip(bill=bill_amount, tiprte=tip_rate)

    # print(f"Calc tot amout : {calc_tot_aomunt[0]}")
    # print(f"Calc tip amt : {calc_tot_aomunt[1]}")
    # bill1 = Bill(527, 7, "x")
    # bill2 = Bill(258, 5, "y")

    # bill1.calc_tip()
    # bill2.calc_tip()