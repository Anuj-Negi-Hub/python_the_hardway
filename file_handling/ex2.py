# Exercise 2 — Write Data to File

# Goal
# Take user input and write into a file.

text = input("Type a message here: ")
try:
    with open("ex2.txt", "w") as file:
        file.write(text)
    print("Data written successfully.")

except IOError:
    print("Error while writing file.")


