#creating two more methods for Student class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Mark: {self.marks}")
    
    #method1: print only name
    def show_name(self):
        print(self.name)
    
    #method2: print only marks
    def show_marks(self):
        print(self.marks)
    
s1 = Student("Rahul", 85)
# print(s1)
s1.display()
s1.show_name()
s1.show_marks()