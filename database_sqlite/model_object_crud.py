import sqlite3


# 1. THE COURSE MODEL OBJECT
class Course:
    """Represents an individual Course data object."""

    def __init__(self, course_name, instructor, credits, course_id=None):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.credits = credits

    def __repr__(self):
        """String representation of the Course object."""
        return f"Course(id={self.course_id}, name='{self.course_name}', instructor='{self.instructor}', credits={self.credits})"


# 2. THE DATABASE MANAGER CLASS
class CourseManager:
    """Handles storing, retrieving, updating, and deleting Course objects."""

    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                instructor TEXT,
                credits INTEGER
            )
        """)
        self.conn.commit()

    # ACCEPT A Course OBJECT
    def add_course(self, course: Course):
        """Inserts a Course object into the database."""
        query = "INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)"
        self.cursor.execute(query, (course.course_name, course.instructor, course.credits))
        self.conn.commit()
        
        # Set the auto-generated ID on the course object
        course.course_id = self.cursor.lastrowid
        print(f"Saved: {course}")

    # RETURN A LIST OF Course OBJECTS
    def get_all_courses(self):
        """Returns a list of Course objects."""
        self.cursor.execute("SELECT * FROM courses")
        rows = self.cursor.fetchall()
        
        # Convert raw database rows (tuples) into Course objects
        courses_list = [Course(course_id=row[0], course_name=row[1], instructor=row[2], credits=row[3]) for row in rows]
        return courses_list

    # UPDATE USING A Course OBJECT
    def update_course(self, course: Course):
        """Updates database record using data from a Course object."""
        query = "UPDATE courses SET instructor = ?, credits = ? WHERE course_name = ?"
        self.cursor.execute(query, (course.instructor, course.credits, course.course_name))
        self.conn.commit()
        print(f"Updated in DB: {course.course_name}")

    # DELETE USING A Course OBJECT
    def delete_course(self, course: Course):
        """Deletes the record corresponding to a Course object."""
        query = "DELETE FROM courses WHERE course_name = ?"
        self.cursor.execute(query, (course.course_name,))
        self.conn.commit()
        print(f"Deleted from DB: {course.course_name}")

    def close(self):
        self.conn.close()


# =========================================================
# WORKING WITH THE OBJECTS
# =========================================================
if __name__ == "__main__":
    db = CourseManager("users.db")

    # STEP 1: Create Course Objects in Python
    course1 = Course("Machine Learning", "Dr. Andrew", 4)
    course2 = Course("Cloud Computing", "Prof. James", 3)

    print("--- 1. Saving Course Objects to DB ---")
    db.add_course(course1)
    db.add_course(course2)
    # db.add_course(1)

    # STEP 2: Fetch data as Course Objects
    print("\n--- 2. Reading Course Objects from DB ---")
    all_courses = db.get_all_courses()
    for c in all_courses:
        print(f"Object: {c.course_name} | Instructor: {c.instructor}")

    # STEP 3: Modify a Course Object & Update DB
    print("\n--- 3. Updating Course Object ---")
    course1.instructor = "Dr. Andrew Ng"  # Modify attribute on the Python object
    course1.credits = 5
    db.update_course(course1)             # Save updated object to DB

    # STEP 4: Delete Course Object
    print("\n--- 4. Deleting Course Object ---")
    db.delete_course(course2)

    db.close()
