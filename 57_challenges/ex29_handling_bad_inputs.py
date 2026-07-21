'''
Write a quick calculator that prompts for the rate of return on an investment and calculates how many years it will take to double your investment.
The formula is  years = 72 / r
where r is the stated rate of return.

Example Output
What is the rate of return? 0
Sorry. That's not a valid input.
What is the rate of return? ABC
Sorry. That's not a valid input.
What is the rate of return? 4
It will take 18 years to double your initial investment.
'''

roi = input("Enter the ROI: ")
has_digit = False
has_letter = False

#checking if input includes letters and letters + digits
for ch in roi:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_digit = True 

if roi == "0":
    print("Sorry, that's not a valid input.")
elif roi < "0":
    print("Sorry, that's not a valid input.")
elif has_digit and has_letter:
    print("Sorry, that's not a valid input")
elif has_letter:
    print("Sorry, it is not a valid input.")
else:
    #calculates when your investment will be double
    result = 72 / float(roi)
    print(f"It will take {result} years to double your initial investments")
    

#same problem usng try and except

roi = input("Enter the ROI: ")
try:
    if roi <= "0":
      print("Sorry, that's not a valid input.")
    else:
        result = 72 / float(roi)
        print(f"It will take {result} years to double your initial investments")

except ValueError:
     print("Sorry, it is not a valid input.")