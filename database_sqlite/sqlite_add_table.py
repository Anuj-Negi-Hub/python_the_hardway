import sqlite3

# Connect to the existing database 'users.db'
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Execute SQL query to create a new table named 'courses'
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    instructor TEXT,
    credits INTEGER
)
""")

# Commit (save) changes and close the connection
conn.commit()
conn.close()

print("New table 'courses' created successfully in users.db!")
