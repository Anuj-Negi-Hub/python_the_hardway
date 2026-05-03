# 1. Create a Car class
# Attributes: brand, model, price
# Method: display_info() → prints all details

# 👉 Task:

# Create 2 car objects
# Print their details


class Car():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"The brand of the car is {self.brand}.")
        print(f"The model of the car is {self.model}.")
        print(f"The price of the car is {self.price}.")
        print(f"A old car is available on resale. The brand of the car is {self.brand}. It is {self.model} model and the price is {self.price}.")

car1 = Car("Tata", 2023, 500000)
car2 = Car("Toyato", 2026, 3000000)

car1.display_info()
car2.display_info()


# ✅ 2. Create a Rectangle class
# Attributes: length, width
# Methods:
# area() → returns area
# perimeter() → returns perimeter

# 👉 Task:

# Create a rectangle and print both values

class Ractangle():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        area = self.lenght * self.width
        return area
    
    def perimeter(self):
        perimeter = 2*(self.lenght + self.width)
        return perimeter
    
ractangle_value = Ractangle(8, 5)
ractangle_area = ractangle_value.area()
ractangle_perimeter = ractangle_value.perimeter()
print("Area:", ractangle_area)
print("Perimeter:", ractangle_perimeter)

# ✅ 3. Create a Student class (simple version)
# Attributes: name, marks
# Method: is_passed()
# return "Pass" if marks ≥ 40
# else "Fail"

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
# name = input("Name of student: ")
# marks = int(input("Marks: "))
s1 = Student("Ankit", 40)
student_status = s1.is_passed()
print(student_status)


# ✅ 4. Bank Account system

# Create a class BankAccount:

# Attributes: name, balance
# Methods:
# deposit(amount)
# withdraw(amount)
# check_balance()

# 👉 Task:

# Create one account
# Perform deposit & withdrawal

class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)  

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ", amount)
        else:
            print("Insufficient balance.")

    
    def check_balance(self):
        print("Balance: ", self.balance)


a1 = BankAccount("Manoj", 15000)
a1.check_balance()
a1.deposit(500)
a1.check_balance()
a1.withdraw(100)
a1.check_balance()


##############################################################3

class F:
    def __init__(self, value):
        self.value = value

    def change(self):
        self.value = 100

f = F(10)
print(f.value)

f.change()
print(f.value)

##############################################################3

# ✅ 5. Book Library System
# Attributes: title, author, is_available
# Methods:
# borrow_book() → book unavailable
# return_book() → book available

class Book():
    
    def __init__(self, title, author, is_avaiable):
        self.title = title
        self.author = author
        self.is_available = True
    
    def borrow_book(self):
        if self.is_available == True:
            print("The book is issued")
            self.is_available = False
        else:
            print("The book is not availables")
    
    def return_book(self):
        print("The book is returned back.")
        self.is_available = True

b1 = Book("Python", "John", True)
b1.borrow_book()

b1.borrow_book()
b1.return_book()
b1.borrow_book()


# ✅ 6. Employee class
# Attributes: name, salary
# Method:
# increase_salary(percent)

# 👉 Example:
# If salary = 10000 and increase = 10% → new salary = 11000

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self, percent):
        self.percent = percent

        self.salary = self.salary + int((self.salary*self.percent)/100)
        return self.salary
        
        
e1 = Employee("John", 10000)
new_salary = e1.increase_salary(10)
print(new_salary)
print()


# ✅ 7. Student Friends System (Upgrade your code)

# Modify your existing code:

# Add method remove_friend()
# Prevent duplicate friends
# Show number of friends


class Student:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friends(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    
    # def add_friend(self, friend):
    # if friend not in self.friends:
    #     self.friends.append(friend)
    # if self not in friend.friends:
    #     friend.friends.append(self)
    
    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
    
    def show_friends(self):
        print(f"{self.name}'s friend", end=" ")
        for f in self.friends:
            print(f.name, end=" ")
        print()

    def count_friend(self):
        return len(self.friends)
    
a = Student("Rahul")
b = Student("Anitha")

a.add_friends(b)
a.show_friends()

b.add_friends(a)
b.show_friends()

print("Total:", a.count_friend())
print("Total:", b.count_friend())


# ✅ 8. ShoppingCart class
# Attributes: items (list)
# Methods:
# add_item(item)
# remove_item(item)
# show_items()

class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def show_items(self):
        for i in self.items:
            print(i, end=" ")
        # print(f"Items: ", self.items)


cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Orage")
cart.show_items()


# ✅ 9. Team and Player

# Create:

# Player class → name, score
# Team class → list of players

# Methods:

# Add player
# Show all players
# Find highest scorer

class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)
    
    def show_players(self):
        for p in self.players:
            print(p.name, p.score)
    
    def highest_scorer(self):
        top = max(self.players, key=lambda x: x.score)
        print("Top scorer:", top.name, top.score)
    

p1 = Player("A", 50)
p2 = Player("B", 80)

team = Team()

team.add_player(p1)
team.add_player(p2)

team.show_players()
team.highest_scorer()













            

