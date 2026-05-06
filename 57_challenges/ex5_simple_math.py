# Write a program that prompts for two numbers.
# Print the sum, difference, product, and quotient of those numbers as shown in the example output:

# Example Output
# What is the first number? 10
# What is the second number? 5
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2

first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

add = first_number + second_number
print(type(add))

diff = first_number - second_number
print(type(diff))

mul = first_number * second_number
print(type(mul))

div = int(first_number / second_number)
print(type(div))

print(type(first_number))
print(type(second_number))

print(f"{add}\n{diff}\n{mul}\n{div}")
print(type(f"{add}\n{diff}\n{mul}\n{div}"))