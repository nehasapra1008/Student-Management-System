from StudentManagementSystem import StudentManagement
st=StudentManagement()
while True:
     print(" Student Managament System")
     print("1.Add Student" )
     print("2.display all student")
     print("3.Search student")
     print("4.Update Marks")
     print("5.Delete student")
     print("6.Exit")

     choice = input("Enter your choice->")

     if choice == "1":
          st.add_Student()
          
     elif choice == "2":
          st.display_Student()
     elif choice == "3":
          st.Serch_Student()
     
     elif choice == "4":
          st.Update_Marks()  

     elif choice == "5":
          st.Delete_student()

     elif choice == "6":
          print("Exit")
          break
     else:
          print("Invalid choice")
                    