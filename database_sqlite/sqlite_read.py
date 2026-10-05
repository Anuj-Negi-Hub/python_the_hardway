import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Fetch all rows
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()

print("--- All Students ---")
for student in all_students:
    print(student)  # Returns a tuple: (id, name, age, grade)

# Fetch specific rows with a condition
cursor.execute("SELECT name, grade FROM students WHERE grade = ?", ("A",))
a_students = cursor.fetchall()

print("\n--- Students with Grade A ---")
for student in a_students:
    print(f"Name: {student[0]}, Grade: {student[1]}")

conn.close()
