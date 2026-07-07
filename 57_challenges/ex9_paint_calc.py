'''
Calculate gallons of paint needed to paint the ceiling of a
room. Prompt for the length and width, and assume one
gallon covers 350 square feet. Display the number of gallons
needed to paint the ceiling as a whole number.
Example Output
You will need to purchase 2 gallons of paint to cover 360 square feet.
Remember, you can’t buy a partial gallon of paint.You must round up to the next whole gallon.
'''

room_len = float(input("Type the lenght of the room: "))
room_wid = float(input("Type the widht of the room: "))

room_area = room_len * room_wid
# print(room_area)
gallon_req = room_area // 350      # Full gallons
area_rem = room_area % 350         # Leftover area

if area_rem > 0:
    gallon_req = gallon_req + 1

print(gallon_req)

#-------------------------------------------------------------------------------------------------------------
#solve this problem using function


def gallon_req(lenght, width):
    room_area = lenght * width
    paint_req = room_area // 350    #Full gallons
    area_rem = room_area % 350     #leftover area
    
    if area_rem > 0:
        paint_req += 1

    print(paint_req) 

room_len = float(input("Type the lenght of the room: "))
room_wid = float(input("Type the widht of the room: "))

gallon_req(room_len, room_wid)