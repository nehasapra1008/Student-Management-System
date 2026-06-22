class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
 
    def display(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print("-" * 20)
 
 
class StudentManagementSystem:
    def __init__(self):
        self.students = []
 
    def add_student(self):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
 
        student = Student(roll_no, name, marks)
        self.students.append(student)
 
        print("Student added successfully!")
 
    def display_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            for student in self.students:
                student.display()
 
    def search_student(self):
        roll_no = int(input("Enter Roll No to search: "))
 
        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found")
                student.display()
                return
 
        print("Student not found.")
 
    def update_marks(self):
        roll_no = int(input("Enter Roll No: "))
 
        for student in self.students:
            if student.roll_no == roll_no:
                new_marks = float(input("Enter New Marks: "))
                student.marks = new_marks
                print("Marks updated successfully!")
                return
 
        print("Student not found.")
 
    def delete_student(self):
        roll_no = int(input("Enter Roll No to delete: "))
 
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
 
        print("Student not found.")
 
 
# Main Program
sms = StudentManagementSystem()
 
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        sms.add_student()
 
    elif choice == "2":
        sms.display_students()
 
    elif choice == "3":
        sms.search_student()
 
    elif choice == "4":
        sms.update_marks()
 
    elif choice == "5":
        sms.delete_student()
 
    elif choice == "6":
        print("Program terminated.")
        break
 
    else:
        print("Invalid choice!")
 
 