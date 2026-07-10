'''
Write a program to compute the value of an investment compounded over time. 
The program should ask for the starting amount, the number of years to invest, the interest rate, and the number of periods per year to compound.
The formula you'll use for this is:

A = P(1 + r/n )nt
where
• P is the principal amount.
• r is the annual rate of interest.
• t is the number of years the amount is invested.
• n is the number of times the interest is compounded peryear.
• A is the amount at the end of the investment.

Example Output
What is the principal amount? 1500
What is the rate? 4.3
What is the number of years? 6
What is the number of times the interest is compounded per year? 4
$1500 invested at 4.3% for 6 years
compounded 4 times per year is $1938.84.
'''

#Need to figure out the value of A as per the above problem. Lets start

p = float(input("Type the principal amount that you invested: "))
r = float(input("Annual rate of interest: "))
t = float(input("Number of years that you want to invest your money: "))
n = float(input("Number of times the interest is compounded per year: "))

r = r/100
total_invest = p * (1 + r / n) ** (n * t)
print(total_invest)

#-------------------------------------------------------------------------------------------------------------
#create the same program using function

def comp_int(p, r, t, n):
    r = r/100
    total = p * (1 + r / n) ** (n * t)
    print(total)

p = float(input("Type the principal amount that you invested: "))
r = float(input("Annual rate of interest: "))
t = float(input("Number of years that you want to invest your money: "))
n = float(input("Number of times the interest is compounded per year: "))
comp_int(p, r, t, n)


#-------------------------------------------------------------------------------------------------------------
#create the same program using class
