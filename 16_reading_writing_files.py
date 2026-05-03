from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want this, hit CTRL-C (^C).")
print("If you do want that, hit Enter.")
input("?")

print("Opening the file....")
target = open(filename, 'w+')
target.write("Hello\n")
target.seek(0)

# print("Truncating the file, goodbye!")
# target.truncate()

print(target.read())

# print("Now I am going to ask you for three lines...")
# line1 = input("line1: ")
# line2 = input("line2: ")
# line3 = input("line3: ")

# print("I am going to write these three lines in the file...")

# target.write(f"{line1}\n{line2}\n{line3}")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally we close the file...")


target.close()


