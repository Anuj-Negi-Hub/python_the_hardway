class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.friends = []

    def display(self):
        print(f"Name: {self.name}, Mark: {self. marks}")

    def add_friend(self, friend):
        self.friends.append(friend)

    def show_friends(self):
        print("Friends:", end=" ")
        for f in self.friends:
            print(f.name, end="")
        print()


student_data = [
    ("Rahul", 85),
    ("Anita", 92),
    ("Vikram", 78),
    ("Sneha", 88),
    ("Arjun", 90)
]

students = [Student(name, marks) for name, marks in student_data]
students[0].add_friend(students[1])
students[0].add_friend(students[2])

students[1].add_friend(students[2])
students[1].add_friend(students[3])

students[2].add_friend(students[3])
students[2].add_friend(students[4])

students[3].add_friend(students[0])
students[3].add_friend(students[4])

students[4].add_friend(students[0])
students[4].add_friend(students[1])

for student in students:
    student.display()
    student.show_friends()
    print()