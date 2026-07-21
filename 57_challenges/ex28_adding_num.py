'''
Write a program that prompts the user for five numbers and computes the total of the numbers.
Example Output
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
The total is 15.
'''

#use loop to prompt for the input instead of writing multiple input statements
result = 0
for i in range(5):
    num = int(input("Enter the number: "))
    result += num
print(result)