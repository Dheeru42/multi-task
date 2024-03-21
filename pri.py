import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_management"
)

cursor = db.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        grade VARCHAR(10)
    )
""")

# Function to add a new student
def add_student(name, age, grade):
    query = "INSERT INTO `students` (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(query, values)
    db.commit()
    print("Student added successfully!")

# Function to view all students
def view_students():
    query = "SELECT * FROM `students`"
    cursor.execute(query)
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        print("ID\tName\tAge\tGrade")
        for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}")

# Main program loop
while True:
    print("\nSchool Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        add_student(name, age, grade)

    elif choice == '2':
        view_students()

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
