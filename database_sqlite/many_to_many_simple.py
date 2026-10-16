import sqlite3

# =============================================================
# 1. THE OBJECTS
# =============================================================
class Student:
    #creating student object
    def __init__(self, name, student_id=None):
        self.student_id = student_id
        self.name = name

    def __repr__(self):
        return f"Student({self.name})"


class Course:
    def __init__(self, title, course_id=None):
        self.course_id = course_id
        self.title = title

    def __repr__(self):
        return f"Course({self.title})"


# =============================================================
# 2. THE DATABASE (3 Tables)
# =============================================================
class SchoolDB:
    def __init__(self, db_name="student_courses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()

    def _create_tables(self):
        # Table 1: Students
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        # Table 2: Courses
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
            )
        """)

        # Table 3: The BRIDGE Table (Connects Student <---> Course)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    # --- Save Objects to DB ---
    def add_student(self, student):
        self.cursor.execute("INSERT INTO students (name) VALUES (?)", (student.name,))
        self.conn.commit()
        student.student_id = self.cursor.lastrowid
        return student

    def add_course(self, course):
        self.cursor.execute("INSERT INTO courses (title) VALUES (?)", (course.title,))
        self.conn.commit()
        course.course_id = self.cursor.lastrowid
        return course

    # --- The Many-to-Many Link ---
 
    def enroll(self, student, course):     #only stores student id and course id
        """Links a Student and a Course together."""
        self.cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
            (student.student_id, course.course_id)
        )
        self.conn.commit()
        print(f"🔗 Enrolled {student.name} in {course.title}")

    # --- Query 1: Find all Courses a Student takes ---
    def get_courses_for_student(self, student):
        query = """
            SELECT c.id, c.title
            FROM courses c
            JOIN enrollments e ON c.id = e.course_id
            WHERE e.student_id = ?
        """
        self.cursor.execute(query, (student.student_id,))
        rows = self.cursor.fetchall()
        print(f"This is the row entries {rows}.")
        print()
        return [Course(title=r[1], course_id=r[0]) for r in rows]

    # --- Query 2: Find all Students inside a Course ---
    def get_students_in_course(self, course):
        query = """
            SELECT s.id, s.name
            FROM students s
            JOIN enrollments e ON s.id = e.student_id
            WHERE e.course_id = ?
        """
        self.cursor.execute(query, (course.course_id,))
        rows = self.cursor.fetchall()
        return [Student(name=r[1], student_id=r[0]) for r in rows]


# =============================================================
# 3. DEMONSTRATION
# =============================================================
if __name__ == "__main__":
    db = SchoolDB()

    # 1. Create Students
    alice = db.add_student(Student("Alice"))
    bob = db.add_student(Student("Bob"))

    # 2. Create Courses
    python_course = db.add_course(Course("Python 101"))
    sql_course = db.add_course(Course("SQL Databases"))

    print("\n--- Enrolling Students ---")
    # Alice takes BOTH Python and SQL
    db.enroll(alice, python_course)
    db.enroll(alice, sql_course)

    # Bob takes only Python
    db.enroll(bob, python_course)

    print("\n--- Which courses is Alice taking? ---")
    alice_courses = db.get_courses_for_student(alice)
    for c in alice_courses:
        print(f"  -> {c.title}, {c.course_id}")

    print("\n--- Who is enrolled in Python 101? ---")
    python_students = db.get_students_in_course(python_course)
    for s in python_students:
        print(f"  -> {s.name}")
