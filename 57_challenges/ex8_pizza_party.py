# Write a program to evenly divide pizzas.
# Prompt for the number of people, the number of pizzas, and the number of slices per pizza. 
# Ensure that the number of pieces comes out even. 
# Display the number of pieces of pizza each person should get. If there are leftovers, show the number of leftover pieces.

people_num = int(input("Enter the total number of peole who wants to eat pizza: "))
pizza_num = int(input("How many Pizzas do you have? "))
slices_pizza = int(input("How many slices each Pizza have? "))
total_pizza_slices = pizza_num * slices_pizza

slices_per_person = total_pizza_slices / people_num
left_over_slices = total_pizza_slices % people_num


print(f"Each person will get {slices_per_person} slices.")
print(f"The leftover pieces of pizzas are {left_over_slices}.")