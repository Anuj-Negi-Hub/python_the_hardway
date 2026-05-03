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



