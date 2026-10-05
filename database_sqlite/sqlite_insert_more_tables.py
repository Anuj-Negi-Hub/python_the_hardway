import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

#insert multiple courses

mech_courses = [
    ("Applied Science", "Prof. Jotsna", 2),
    ("Aerodynamic", "Prof. Munda", 3),
    ("Electronics", "Prof. Krishna", 4),
    ("Car", "Prof. Rajshekar", 5)
]

#execute multiple couses
cursor.executemany(
    "INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)",
    mech_courses
)

conn.commit()
conn.close()

