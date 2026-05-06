#create a program that prompts for a quote and an author.
#Display the quotation and author as shown in the example output.

#Example output
# What is the quote? These aren't the droids you're looking for.
# Who said it? Obi-Wan Kenobi
# Obi-Wan Kenobi says, "These aren't the droids you're looking for."

# Constraints:
# Use a single output statement to produce this output, using appropriate string-escaping techniques for quotes.
# If your language supports string interpolation or string substitution, don't use it for this exercise. Use string concatenation.

quotes = input("What is the quotes? ")
author_name = input("Who said it? ")

print(f"{author_name} says, \"{quotes}\"")