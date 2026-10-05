'''
Exercise 2: Positive, Negative, or Zero

Ask the user for a number and print whether it is:
    Positive
    Negative
    Zero
'''

def sign_num(num):
    if num == 0:
        print(f"The number {num} is zero.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is positive.")

num = float(input("Type any number (positive, negative, or zero): "))
sign_num(num)