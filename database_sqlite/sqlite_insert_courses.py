import sqlite3

# Connect to the database 'users.db'
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 1. Insert a single course
cursor.execute(
    "INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)",
    ("Python Programming", "Dr. Smith", 4)
)

# 2. Insert multiple courses at once
many_courses = [
    ("Data Structures", "Prof. Johnson", 3),
    ("Database Systems", "Dr. Williams", 4),
    ("Web Development", "Prof. Davis", 3)
]

cursor.executemany(
    "INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)",
    many_courses
)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Inserted courses successfully into 'users.db'!")
