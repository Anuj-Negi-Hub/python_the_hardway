'''
Write a program that asks the user for their age and compare it to the legal driving age of eighteen. 
If the user is eighteen or older, then the program should display “You are old enough to legally drive.”
If the user is under eighteen, the program should display “You are not old enough to legally drive.”

Example Output
What is your age? 15
You are not old enough to legally drive.
Or
What is your age? 35
You are old enough to legally drive.
'''


age = float(input("Type your current age: "))
legal_age = 18

if age >= legal_age:
    print("You are old enough to legally drive.")
else:
    print("You are not old enough to legally drive.")

print()
#-------------------------------------------------------------------------------------------------------------
#create the same program using function
def drv_lin(cur_age, leg_age):
    if cur_age >= leg_age:
        print("You are old enough to legally drive.")
    else:
        print("You are not old enough to legally drive.")

cur_age = float(input("Type your current age: "))
leg_age = 18
drv_lin(cur_age, leg_age)