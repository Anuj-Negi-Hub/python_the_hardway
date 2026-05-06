# Create a program that calculates the area of a room. 
# Prompt the user for the length and width of the room in feet.
# Then display the area in both square feet and square meters.

import os

def area(length, width):
    #formula to calculate the area of a ractanguler
    room_area = length * width

    SQFT_TO_SQM = 0.09290304                    #constant

    #formula to convert square feet to square meter
    area_meter = room_area * SQFT_TO_SQM

    return room_area, area_meter

    # print(f"The area of the room is {room_area} square feet.")
    # print(f"The area of the room is {area_meter} square meter.")
     
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))

print(f"You entered dimensions of {length} feet by {width} feet.")

# unpacking
sqft, sqm = area(length, width)

print(f"The area of the room is {sqft} square feet.")
print(f"The area of the room is {sqm} square meter.")

# s1 = area(length, width)
# print(s1)

new_file = open("ex7.txt", "w+")

content_to_paste = new_file.write(
    f"The area of the room is {sqft} square feet.\n"
    f"The area of the room is {sqm} square meter."
    )
new_file.close()



