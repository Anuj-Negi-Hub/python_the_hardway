'''
Create a program that generates multiplication tables for the numbers 0 through 12.

Example Output
0 X 0 = 0
0 X 1 = 0
...
12 x 11 = 132
12 x 12 = 144
'''

num_table = int(input("Type a number between 0 to 12: "))

#ensures if the enter number is not less than 0 and more than 12
if num_table > 12 or num_table < 0:
    print("Type the correct number.")

else:
    for i in range(1, 11):
        print(num_table , "x", i, "=", num_table * i)



