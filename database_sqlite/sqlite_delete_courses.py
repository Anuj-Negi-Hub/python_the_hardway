import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

#delete only one row

cursor.execute("DELETE FROM courses WHERE course_name = ?", ("Aerodynamic",))
print(f"Deleted {cursor.rowcount} row(s) where course_name = 'Aerodynamic'")

conn.commit()
conn.close()


