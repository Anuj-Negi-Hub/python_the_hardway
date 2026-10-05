import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# UPDATE data
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Bob"))
print(f"Updated {cursor.rowcount} row(s)")

# DELETE data
cursor.execute("DELETE FROM students WHERE name = ?", ("Diana",))
print(f"Deleted {cursor.rowcount} row(s)")

conn.commit()
conn.close()
