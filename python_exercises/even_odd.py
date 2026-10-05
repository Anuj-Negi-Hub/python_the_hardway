'''
Exercise 1: Even or Odd
Ask the user to enter a number and determine whether it is even or odd.

Example:
Enter a number: 17
17 is odd.
'''

def even_odd(num):
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")



num = int(input("Type a number: "))
even_odd(num)