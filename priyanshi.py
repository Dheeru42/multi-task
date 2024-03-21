class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}")


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"\nStudents in {self.name}:\n")
        for student in self.students:
            student.display_info()


def main():
    school_name = input("Enter school name: ")
    school = School(school_name)

    while True:
        print("\nSchool Management System Menu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_number = input("Enter student roll number: ")
            grade = input("Enter student grade: ")
            student = Student(name, roll_number, grade)
            school.add_student(student)
            print("Student added successfully!")

        elif choice == '2':
            school.display_students()

        elif choice == '3':
            print("Exiting School Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
