def calc_tip(bill, tiprte):
    """Calculate the tip value and total amount.
    Need to print the total amount and tip"""
    tip_val = (bill * tiprte) / 100
    tot_amt = bill + tip_val

    # print(f"This is my tip amount {tip_val}.")
    # print(f"The total amount of the bill is {tot_amt}.")
    return [tot_amt, tip_val]

class Bill:
    def __init__(self, bill, tip_rate, cust_name):
        self.bill_amnt = bill
        self.tip = tip_rate
        self.name = cust_name

    def calc_tip(self):
        """Calculate the tip value and total amount.
        Need to print the total amount and tip"""
        tip_val = (self.bill_amnt * self.tip) / 100
        tot_amt = self.bill_amnt + tip_val
        print(f"The customer name: {self.name}")
        print(f"This is my tip amount {tip_val}.")
        print(f"The total amount of the bill is {tot_amt}.")

if __name__ == "__main__":
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
    bill1 = Bill(527, 7, "x")
    bill2 = Bill(258, 5, "y")

    bill1.calc_tip()
    bill2.calc_tip()