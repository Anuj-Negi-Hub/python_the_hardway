from sys import argv
# read thw WYSS section for how to run this

script, first, second, third = argv

get_input = input("Tell the name who wrote this code: ")

print("The script is called:", script)
print("The first variable is called:", first)
print("The second variable is called:", second)
print("The thrid variable is called:", third)

#Combine input with argv to make a script that gets more input from a user. Don’t overthink
#it. Just use argv to get something, and input to get something else from the user.


print(f"{get_input} wrote this code.")