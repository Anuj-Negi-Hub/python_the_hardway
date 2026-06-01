the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "oranges", "pears", "appricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count: {number}")

#same as above
for fruit in fruits:
    print(f"A type of fruit: {fruit}")

#also we can go through mixed list too
#notice we have to use {} since we don't kow what's in it

for i in change:
    print(f"I got {i}.")


#we can also build lists, first start with an empty one

elements = []

#then use the range function to do 0 to 5 count

for i in range(0, 6):
    print(f"Adding {i} to the list")
    #append is a function that list understand
    elements.append(i)
print(elements)
#now we can print them out too

for i in elements:
    print(f"The element was: {i}")


