'''
Create a program to calculate the body mass index (BMI) for a person using the person's height in inches and weight in pounds.
The program should prompt the user for weight and height.

Calculate the BMI by using the following formula:
bmi = (weight / (height x height)) * 703

If the BMI is between 18.5 and 25, display that the person is at a normal weight.
If they are out of that range, tell them if they are underweight or overweight and tell them to consult their doctor.

Example Output:
Your BMI is 19.5.
You are within the ideal weight range. (or)

Your BMI is 32.5.
You are overweight. You should see your doctor.
'''

#Create aproblem to calculate BMI by taking the inputs from the user

weight = float(input("Type your weight in pounds: "))
height = float(input("Type your height in inches: "))

#formula to calculate BMI

bmi = (weight / (height * height)) * 703

if bmi >= 18.5 and bmi <= 25: 
    print(f"Your bmi is {bmi} which indicates that you are within the ideal weight range")

elif bmi < 18.5:
    print(f"Your bmi is {bmi} which indicates that you are under weight. Please consult your doctor.")

else:
    print(f"Your bmi is {bmi} which indicates that you are over weight. Please consult your doctor.")


# solve the same problem using function

def bmi_cal(weight, height):
    #formula to calculate bmi
    bmi = (weight / (height * height)) * 703

    if bmi >= 18.5 and bmi <= 25: 
        print(f"Your bmi is {bmi} which indicates that you are within the ideal weight range")

    elif bmi < 18.5:
        print(f"Your bmi is {bmi} which indicates that you are under weight. Please consult your doctor.")

    else:
        print(f"Your bmi is {bmi} which indicates that you are over weight. Please consult your doctor.")

weight = float(input("Type your weight in pounds: "))
height = float(input("Type your height in inches: "))

bmi_cal(weight, height)

