import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

#update the instructor name where course_name is "python programming"

# cursor.execute(
#     "UPDATE courses SET instructor = ? where course_name = ?",
#     ("Dr. Alex", "Python Programming")
# )

cursor.execute(
    "UPDATE courses SET instructor = ?, credits = ? WHERE course_name = ?",
    ("Prof. David", 4, "Data Structures")
)
print(f"Upated {cursor.rowcount} row(s)")

conn.commit()
conn.close()