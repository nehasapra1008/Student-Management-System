from Student import Student
class StudentManagement:
    def __init__(self):
        print("Welcome to Student Management System")
        self.students=[]
       
    def add_Student(self):
        roll_no=int(input("Enter the roll_no->"))
        name=input("Enter the name->")
        marks=int(input("Enter the marks->"))
        st=Student(roll_no,name,marks)
        self.students.append(st)
        print("Student added successfully.")

    def display_Student(self):
        for student in self.students:
            student.display()

    def Serch_Student(self):
        print("search student")

    def Update_Marks(self):
        print("update marks")

    def Delete_student(self):
        print("delete student")    