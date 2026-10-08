import sqlite3

# -------------------------------------------------------------
# 1. DATABASE MANAGER
# -------------------------------------------------------------
class Database:
    """Manages the database connection."""
    def __init__(self, db_name="school.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                grade TEXT
            )
        """)
        self.conn.commit()


# -------------------------------------------------------------
# 2. STUDENT OBJECT (Active Record Pattern)
# -------------------------------------------------------------
class Student:
    def __init__(self, name, email, grade, student_id=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.grade = grade

    # THE OBJECT SAVES ITSELF TO THE DATABASE
    def save(self, db: Database):
        """Saves or updates this student in the database."""
        if self.student_id is None:
            # New Student -> INSERT
            query = "INSERT INTO students (name, email, grade) VALUES (?, ?, ?)"
            db.cursor.execute(query, (self.name, self.email, self.grade))
            db.conn.commit()
            self.student_id = db.cursor.lastrowid
            print(f"✅ Saved new student '{self.name}' with ID {self.student_id}")
        else:
            # Existing Student -> UPDATE
            query = "UPDATE students SET name=?, email=?, grade=? WHERE id=?"
            db.cursor.execute(query, (self.name, self.email, self.grade, self.student_id))
            db.conn.commit()
            print(f"🔄 Updated student '{self.name}' (ID: {self.student_id})")

    # OBJECT METHOD TO CHANGE GRADE AND UPDATE DB
    def update_grade(self, new_grade, db: Database):
        """Modifies Python attribute and updates database immediately."""
        self.grade = new_grade  # Change in Python memory
        self.save(db)           # Sync with SQLite database

    # THE OBJECT DELETES ITSELF FROM DATABASE
    def delete(self, db: Database):
        """Deletes this student from database."""
        if self.student_id:
            query = "DELETE FROM students WHERE id=?"
            db.cursor.execute(query, (self.student_id,))
            db.conn.commit()
            print(f"❌ Deleted student '{self.name}' from database")
            self.student_id = None

    def __repr__(self):
        return f"Student(ID={self.student_id}, Name='{self.name}', Email='{self.email}', Grade='{self.grade}')"


# -------------------------------------------------------------
# HOW IT WORKS IN PRACTICE
# -------------------------------------------------------------
if __name__ == "__main__":
    db = Database("school.db")

    # 1. Create a Student Object in memory
    s1 = Student("Alice Smith", "alice@email.com", "B")

    # 2. Tell the object to save itself into DB
    s1.save(db)

    # 3. Modify grade on the object and sync with DB
    print("\n--- Changing Grade ---")
    s1.update_grade("A+", db)

    # 4. Print the current object status
    print("Current Object State:", s1)

    # 5. Tell the object to delete itself
    print("\n--- Deleting Student ---")
    s1.delete(db)
