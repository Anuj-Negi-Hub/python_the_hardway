a = input("Type first number: ")
b = input("Type second number: ")

c = int(a) + int(b)


print(f"The sum of {a} and {b} is {c}.")


# Write the statement "The sum of a and b is c" in 21_new_file.txt.



out_file = open("21_new_file.txt", 'a')

out_file.write(f"The sum of {a} and {b} is {c}.\n")

print("Alright, all done!")
out_file.close()