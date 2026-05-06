# create a program that determines how many years you have left until retirement and the year you can retire.
# It should prompt for your current age and the age you want to retire
# and display the output as shown in the example that follows.

# Example output
# What is the current age? 25
# At what age would you like to retire? 65
# You have 40 years left until you can retire.
# It's 2015, so you can retire in 2055.

from datetime import date

# get the current year from the system
current_year = date.today().year

# prompt for inputs and convert them to integers
age = int(input("What is your current age? "))
rtr_age = int(input("At what age would you like to retire? "))

# perform the calculations
years_left = rtr_age - age
retirement_years = current_year + years_left

print(f"You have {years_left} years left until you can retire.")
print("It's", current_year, "so you can retire in", current_year + years_left, ".")
print(f"It's {current_year} so you can retire in {(current_year + years_left)}.")
print(f"It's {current_year} so you can retire in {retirement_years}.")