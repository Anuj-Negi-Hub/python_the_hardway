import sqlite3

class CourseManager:
    """Class to manage all CRUD operations for the 'courses' table in SQLite."""

    def __init__(self, db_name="users.db"):
        # 1. Connect to database and create a cursor
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
        # Automatically ensure table exists
        self._create_table()

    def _create_table(self):
        """Private helper method to create the courses table."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                instructor TEXT,
                credits INTEGER
            )
        """)
        self.conn.commit()

    # ------------------ C - CREATE ------------------
    def add_course(self, course_name, instructor, credits):
        """Insert a new course into the database."""
        query = "INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)"
        self.cursor.execute(query, (course_name, instructor, credits))
        self.conn.commit()
        print(f"Added course: '{course_name}' (ID: {self.cursor.lastrowid})")

    # ------------------ R - READ ------------------
    def get_all_courses(self):
        """Fetch and return all courses from the database."""
        query = "SELECT * FROM courses"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_course_by_name(self, course_name):
        """Fetch a specific course by its name."""
        query = "SELECT * FROM courses WHERE course_name = ?"
        self.cursor.execute(query, (course_name,))
        return self.cursor.fetchone()

    # ------------------ U - UPDATE ------------------
    def update_course(self, course_name, new_instructor, new_credits):
        """Update instructor and credits for a specific course."""
        query = "UPDATE courses SET instructor = ?, credits = ? WHERE course_name = ?"
        self.cursor.execute(query, (new_instructor, new_credits, course_name))
        self.conn.commit()
        print(f"Updated {self.cursor.rowcount} course(s).")

    # ------------------ D - DELETE ------------------
    def delete_course(self, course_name):
        """Delete a course by its name."""
        query = "DELETE FROM courses WHERE course_name = ?"
        self.cursor.execute(query, (course_name,))
        self.conn.commit()
        print(f"Deleted {self.cursor.rowcount} course(s).")

    # ------------------ CLEANUP ------------------
    def close(self):
        """Close the database connection."""
        self.conn.close()
        print("Database connection closed.")


# =========================================================
# HOW TO USE THE OBJECT (Example Usage)
# =========================================================
if __name__ == "__main__":
    # 1. Instantiate the object
    manager = CourseManager("users.db")

    # 2. CREATE (Insert data)
    manager.add_course("Python Core", "Dr. Alex", 4)
    manager.add_course("Web Dev", "Prof. Sarah", 3)

    # 3. READ (Fetch all courses)
    print("\n--- All Courses ---")
    courses = manager.get_all_courses()
    for c in courses:
        print(c)

    # 4. UPDATE (Modify data)
    print("\n--- Updating Course ---")
    manager.update_course("Python Core", "Dr. Alexander", 5)

    # 5. READ ONE (Fetch updated record)
    print("Updated Record:", manager.get_course_by_name("Python Core"))

    # 6. DELETE (Remove data)
    print("\n--- Deleting Course ---")
    manager.delete_course("Web Dev")

    # 7. Close Connection
    manager.close()
