class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # dictionary {subject: marks}

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


students = []

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = {}
    for subject in ["Math", "Science", "English"]:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    student = Student(roll_no, name, marks)
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            student.display()

def search_student():
    roll_no = input("Enter Roll No to search: ")
    for student in students:
        if student.roll_no == roll_no:
            student.display()
            return
    print("Student not found.")

def update_student():
    roll_no = input("Enter Roll No to update: ")
    for student in students:
        if student.roll_no == roll_no:
            student.name = input("Enter new name: ")
            for subject in student.marks:
                student.marks[subject] = int(input(f"Enter new marks for {subject}: "))
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
