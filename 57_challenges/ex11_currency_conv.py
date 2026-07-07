'''
Write a program that converts currency. Specifically, convert euros to U.S. dollars. 
Prompt for the amount of money in euros you have, and prompt for the current exchange rate of the euro. 
Print out the new amount in U.S. dollars. The formula for currency conversion is
amount to = (amount from × rate from) / rate to

where
• Amount to is the amount in U.S. dollars.
• Amount from is the amount in euros.
• rate from is the current exchange rate in euros.
• rate to is the current exchange rate of the U.S. dollar.

Example Output
How many euros are you exchanging? 81
What is the exchange rate? 137.51
81 euros at an exchange rate of 137.51 is 111.38 U.S. dollars.
'''


euro_have = int(input("Enter how much euroes you want to exhange with the US dollar: "))
exch_rate = float(input("Type the conversation rate from euro to US dollar: "))

total_dollar = euro_have * exch_rate

print(f"{euro_have} euros at an exchange rate of {exch_rate} is {total_dollar} US dollar.")

#-------------------------------------------------------------------------------------------------------------
#create the same program using function

def currency_con(euroes, exc_rate):
    total_dollar = euroes * exc_rate
    print(total_dollar)

euro_have = int(input("How much euroes do you have: "))
exch_rate = float(input("Type the conversation rate from euro to US dollar: "))

currency_con(euro_have, exch_rate)