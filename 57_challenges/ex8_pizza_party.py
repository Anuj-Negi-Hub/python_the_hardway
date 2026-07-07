# Write a program to evenly divide pizzas.
# Prompt for the number of people, the number of pizzas, and the number of slices per pizza. 
# Ensure that the number of pieces comes out even. 
# Display the number of pieces of pizza each person should get. If there are leftovers, show the number of leftover pieces.

people_num = int(input("Enter the total number of peole who wants to eat pizza: "))
pizza_num = int(input("How many Pizzas do you have? "))
slices_pizza = int(input("How many slices each Pizza have? "))
total_pizza_slices = pizza_num * slices_pizza

slices_per_person = total_pizza_slices // people_num
left_over_slices = total_pizza_slices % people_num


print(f"Each person will get {slices_per_person} slices.")
print(f"The leftover pieces of pizzas are {left_over_slices}.")


#-------------------------------------------------------------------------------------------------------------
#Solve the same problem using function

def div_pizza(people_num, pizza_num, slices_pizza):

    total_pizza_slices = pizza_num * slices_pizza
    slices_per_person = total_pizza_slices // people_num
    left_over_slices = total_pizza_slices % people_num

    print(f"Each person will get {slices_per_person} slices.")
    print(f"The leftover pieces of pizzas are {left_over_slices}.")


people_num = int(input("Enter the total number of peole who wants to eat pizza: "))
pizza_num = int(input("How many Pizzas do you have? "))
slices_pizza = int(input("How many slices each Pizza have? "))

div_pizza(people_num, pizza_num, slices_pizza)

#-------------------------------------------------------------------------------------------------------------
#Solve the same problem using class   

class Party:
    def __init__(self, people_num, pizza_num, slices_pizza):
        self.people = people_num
        self.pizza = pizza_num
        self.slice = slices_pizza
    
    #create a function to calculate total slices
    def total_slices(self):
        total_pizza_slices = self.pizza * self.slice
        return total_pizza_slices

    #create a function to calculate slices per person
    def slices_per_person(self):
        #calling the another function using self
        total_pizza_slices = self.total_slices()
        slices_per_person = total_pizza_slices // self.people
        return slices_per_person
    
    #create a function to calculate left over slices
    def left_over_slices(self):
        total_pizza_slices = self.total_slices()
        left_over_slices = total_pizza_slices % self.people
        return left_over_slices

people_num = int(input("Enter the total number of peole who wants to eat pizza: "))
pizza_num = int(input("How many Pizzas do you have? "))
slices_pizza = int(input("How many slices each Pizza have? "))

#unpacking
pizza_party = Party(people_num, pizza_num, slices_pizza)
print(f"Total slices: {pizza_party.total_slices()}")
print(f"Total slices per person: {pizza_party.slices_per_person()}")
print(f"Total slices left: {pizza_party.left_over_slices()}")




