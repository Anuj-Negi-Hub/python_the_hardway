'''
Write a program that converts a number from 1 to 12 to the corresponding month.
Prompt for a number and display the corresponding calendar month, with 1 being January and 12 being December.
For any value outside that range, display an appropriate error message.

Example Output
Please enter the number of the month: 3
The name of the month is March.
'''
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_num = int(input("Type the month number (for example, 2 =February, 6 = June): "))

#substract 1 from the month_num as he first item in month_list is at 0 position
month_seq = month_num - 1

if month_num >=1 and month_num <= 12:
    # sel_month = month_list[month_name]
    print(f"The name of the month is {month_list[month_seq]}.")

else:
    print(f"You have typed {month_num}. Please enter the correct month number.")


#solve the same problem using function


def month_name(month_list, month_num):
    #substract 1 from the month_num as he first item in month_list is at 0 position
    month_seq = month_num - 1

    if month_num >=1 and month_num <= 12:
        # sel_month = month_list[month_name]
        print(f"The name of the month is {month_list[month_seq]}.")

    else:
        print(f"You have typed {month_num}. Please enter the correct month number.")

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_num = int(input("Type the month number (for example, 2 =February, 6 = June): "))

month_name(month_list, month_num)