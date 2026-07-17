'''
Write a program that asks for three numbers. Check first to see that all numbers are different.
If they're not different, then exit the program. Otherwise, display the largest number of the three.

Example Output:
Enter the first number: 1
Enter the second number: 51
Enter the third number: 2
The largest number is 51.
'''

first_num = int(input("Type the first number: "))
second_num = int(input("Type the second number: "))
third_num = int(input("Type the third number: "))

#check if all numbers are same
if first_num == second_num or first_num == third_num or second_num == third_num:
    print("All the numbers should be different. Please type the different numbers")

# check if first number is largest
elif first_num > second_num and first_num > third_num:
    print(f"First number is the biggest.")

# check if second number is largest
elif second_num > first_num and second_num > third_num:
    print(f"Second number is the biggest.")

# check if third number is largest
elif third_num > first_num and third_num > second_num:
    print(f"Third number is the biggest.")

# Solve the same problem using function

def largest_num(first_num, second_num, third_num):
    #check if all numbers are same
    if first_num == second_num or first_num == third_num or second_num == third_num:
        print("All the numbers should be different. Please type the different numbers")

    # check if first number is largest
    elif first_num > second_num and first_num > third_num:
        print(f"First number is the biggest.")

    # check if second number is largest
    elif second_num > first_num and second_num > third_num:
        print(f"Second number is the biggest.")

    # check if third number is largest
    elif third_num > first_num and third_num > second_num:
        print(f"Third number is the biggest.")

first_num = int(input("Type the first number: "))
second_num = int(input("Type the second number: "))
third_num = int(input("Type the third number: "))

largest_num(first_num, second_num, third_num)
