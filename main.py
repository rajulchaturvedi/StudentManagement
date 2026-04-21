# main.py
from auth import login
import student_manager as sm

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sm.add_student()
        elif choice == "2":
            sm.view_students()
        elif choice == "3":
            sm.search_student()
        elif choice == "4":
            sm.update_student()
        elif choice == "5":
            sm.delete_student()
        elif choice == "6":
            sm.sort_students()
        elif choice == "7":
            sm.generate_report()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    if login():
        menu()