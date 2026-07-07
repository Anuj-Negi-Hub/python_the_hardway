'''
Create a program that computes simple interest. Prompt for the principal amount, the rate as a percentage, and the time,
and display the amount accrued (principal + interest).

The formula for simple interest is A = P(1 + rt), where P is the principal amount, r is the annual rate of interest, t is the
number of years the amount is invested, and A is the amount at the end of the investment.

Example Output
Enter the principal: 1500
Enter the rate of interest: 4.3
Enter the number of years: 4
After 4 years at 4.3%, the investment will be worth $1758.
'''

# formula: A = P(1 + rt)

prin_amnt = float(input("Type the principle amount: ")) 
roi = float(input("Type the annual rate of interest: "))
num_year =  float(input("Type the number of years the amount is invested: "))

total_invest = prin_amnt * (1 + roi * num_year)
print(total_invest)

#-------------------------------------------------------------------------------------------------------------
#create the same program using function

def sim_int(p_amnt, r, n):
    total = p_amnt * (1 + r * n)
    return total

p_amnt = float(input("Type the principle amount: ")) 
r = float(input("Type the annual rate of interest: "))
n =  float(input("Type the number of years the amount is invested: "))

total_amount = sim_int(p_amnt, r, n)
print(total_amount)