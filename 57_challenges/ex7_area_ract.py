# Create a program that calculates the area of a room. 
# Prompt the user for the length and width of the room in feet.
# Then display the area in both square feet and square meters.

def area(length, width):
    #formula to calculate the area of a ractanguler
    room_area = length * width

    SQFT_TO_SQM = 0.09290304                    #constant

    #formula to convert square feet to square meter
    area_meter = room_area * SQFT_TO_SQM

    print(f"The area of the room is {room_area} square feet.")
    print(f"The area of the room is {area_meter} square meter.")
     
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))

print(f"You entered dimensions of {length} feet by {width} feet.")

area(length, width)