#defining a function called cheese_and_crackers with two parameters, cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):

    #print the quantity of cheese with the contents inside the print function
    print(f"You have {cheese_count} cheese.")

    #print the count of crackers boxes with the contents inside the print function
    print(f"You have {boxes_of_crackers} boxes of crackers.")

    #again print with the contents inside the print function
    print("That's enough for a party.")

    #again print with the contents inside the print function
    print("Get a blanket\n")

    # return None

#print the statements inside the print function
print("We can just give the function numbers directly")

#here we are calling the function by giving two values. Where cheese_count = 20 and boxes_of_crackers = 30. 
# This line call the function and pass variables (20 to cheese_count and 30 to boxes_of_crackers) as arguments to the function
# and then  execute the function and will provide the output
cheese_and_crackers(20, 30)

#print the statements inside the print function
print("OR, we can use variables from our script: ")

#Creating a variable (amount_of_cheese) and storing the value of 10.
amount_of_cheese = 10

#Creating a variable (amount_of_crackers) and storing the value of 50.
amount_of_crackers = 50

#we are passing these two variables to our function instead of giving the value directly inside the braces.
#call the function with the values 10 and 50 and give the output.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#print the statement inside the print function
print("We can even do math inside too.")

#again here we are giving the values as 10 + 20 and 5 + 6 to the function
#
cheese_and_crackers(10 + 20, 5 + 6)

#printing the statements inside the print function
print("And, we can combine the two, variables and math.")

#here we are passing variables and integer 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
