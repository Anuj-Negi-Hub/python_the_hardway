#create a program that prompts for an input string
# and displays output that shows the input string and the number of the characters the string contains

# Example Output
# What is the input string? Homer
# Homer has 5 characters.

# Constraints Warning
# Be sure the output contains the original String
# Use a single output statement to construct the output
# Use a built-in function of the programming language to determine the length of the string.

input_string = input("Type a word: ")
print(input_string)
len_str = len(input_string)
print(f"'{input_string}' contains {len_str} characters.")