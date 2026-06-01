from sys import argv
# read the WYSS section for how to run this
print(argv, end ="\n")
script, first, second, third = argv
print()
print("The script is called:", script, end = "\n")
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)