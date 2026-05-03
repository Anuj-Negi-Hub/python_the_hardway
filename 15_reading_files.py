from sys import argv

script, filename = argv

txt = open(filename)
print(f"Here is your file {filename}:")
print(txt.read())

print("Type the file name again:")
# file_again = input(">")
file_again = filename
# txt_again = open(file_again)

print(file_again.read())

txt.close()
# txt_again.close()



# second program start from here


# import time
import os
import time
print(os.getcwd())

filename = input("Type the file name: ")
txt = open(filename)
print("The file is getting open.....")
time.sleep(1)

print("printing.....")
time.sleep(1)
print("printing.....")
time.sleep(1)
print("printing.....")
time.sleep(1)
print()

print(txt.read())
txt.close()
print()

print("The file is getting closed....")
time.sleep(2)

print("The file is closed now.")