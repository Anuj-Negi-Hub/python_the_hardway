#make a student class with student name and his marks in one subject

#create two more methods for Student class
# Attach two students as friends to other students

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Mark: {self.marks}")
    
    
# s1 = Student("Rahul", 85)
# s1.display()
# s1.show_name()
# s1.show_marks()

# Create four more student objects using list and for loops
# List of student data
student_data = [
    ("Rahul", 85),
    ("Anita", 92),
    ("Vikram", 78),
    ("Sneha", 88),
    ("Arjun", 90)
]

# Create objects using list
students = []

print(len(student_data))

for index, data in enumerate(student_data):
    print(data, end=" ")
    print(index)

    if index == len(student_data) - 1:  #check this and figure out
        print(end="")
    
# print()

for name, marks in student_data:
    students.append(Student(name, marks)) 

# Display all student objects
for student in students:
    student.display()



