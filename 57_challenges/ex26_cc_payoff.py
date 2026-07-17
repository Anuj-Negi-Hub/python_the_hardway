'''
Write a program that will help you determine how many months it will take to pay off a credit card balance.
The program should ask the user to enter the balance of a credit card and the APR of the card.
The program should then return the number of months needed.
The formula for this is:

 n = - 1/ 30 x (log(1 + b / p (1 - (1 + i) ** 30)) / log(1 + i))

where
• n is the number of months.
• i is the daily rate (APR divided by 365).
• b is the balance.
• p is the monthly payment.

Example Output
What is your balance? 5000
What is the APR on the card (as a percent)? 12
What is the monthly payment you can make? 100
It will take you 70 months to pay off this card.
'''
import math

APR = int(input("Type the APR per month for your credit card: "))
total_APR = APR / (365 * 100)
amt_bal = int(input("Enter the balance amount of the credit card: "))
mon_pay = int(input("How much monthly payment would you like to pay: "))
value = math.log(1 + amt_bal / mon_pay * (1 - (1 + total_APR) ** -30))
print(value)

num_mon = - (1 / 30) * value / math.log(1 + total_APR)

print(num_mon)