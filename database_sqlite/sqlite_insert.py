import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Insert a single row using parameterized query (?)
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 20, "A"))

# Insert multiple rows at once
many_students = [
    ("Bob", 22, "B"),
    ("Charlie", 19, "A"),
    ("Diana", 21, "C")
]
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", many_students)

conn.commit()
print(f"Inserted rows successfully!")
conn.close()
