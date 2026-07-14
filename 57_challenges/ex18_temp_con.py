'''
Create a program that converts temperatures from Fahrenheit to Celsius or from Celsius to Fahrenheit. 
Prompt for the starting temperature. The program should prompt for the type of conversion and then perform the conversion.

The formulas are
C = (F - 32) x 5 / 9
and
F = (C x 9 / 5) + 32

Example Output:
Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice: C
Please enter the temperature in Fahrenheit: 32
The temperature in Celsius is 0.
'''

temp = input("Press 'C' to convert from 'Fahrenheit to Celsius' or press 'F' to convert from 'Celsius to Fahrenheit': ").lower()

if temp == "c" or temp == "f":

    if temp == "c":
        temp_fah = float(input("Type the temperature in fahrengeit: "))

        #formula to convert temperature from fahrenhiet to celcius
        temp_in_cel = (temp_fah - 32) * 5 / 9
        print(f"The temperature in celcius is {temp_in_cel} degree celcius.")

    elif temp == "f":
        temp_cel = float(input("Type the temperature in celcius: "))

        #formula to convert temperature from celcius to fahrenhiet
        temp_in_fah = (temp_cel * 9 / 5) + 32
        print(f"The temperature in fahrenheit is {temp_in_fah} degree fahrenheit.")

else:
    print(f"You typed {temp} which is a wrong keyword. Please type F or C.")


# solve the same problem using function

def temp_con(temp):
    if temp == "c" or temp == "f":

        if temp == "c":
            temp_fah = float(input("Type the temperature in fahrengeit: "))

            #formula to convert temperature from fahrenhiet to celcius
            temp_in_cel = (temp_fah - 32) * 5 / 9
            print(f"The temperature in celcius is {temp_in_cel} degree celcius.")

        elif temp == "f":
            temp_cel = float(input("Type the temperature in celcius: "))

            #formula to convert temperature from celcius to fahrenhiet
            temp_in_fah = (temp_cel * 9 / 5) + 32
            print(f"The temperature in fahrenheit is {temp_in_fah} degree fahrenheit.")

    else:
        print(f"You typed {temp} which is a wrong keyword. Please type F or C.")

temp = input("Press 'C' to convert from 'Fahrenheit to Celsius' or press 'F' to convert from 'Celsius to Fahrenheit': ").lower()
temp_con(temp)