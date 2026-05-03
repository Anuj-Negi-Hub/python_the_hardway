name = "Zed A. Shaw"
age = 35 #not a lie
height = 74 #in inches

#round function is used to round off the value. That means even if the value is flot, it will give integer.
heights_cm = round(74 * 2.54) 
weight = 180 #in lsb
weight_kg = round(180 * 0.453592)
eyes = "Blue"
teeth = "White"
hair = "Brown"


print(f"Lets talk about {name}.")
print(f"He's {heights_cm} cm tall.")
print(f"He is {weight_kg} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He has got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky. Try to get it exactly right

total = age + heights_cm + weight_kg
print(f"If I had {age} , {heights_cm}, and {weight_kg} I get {total}.")