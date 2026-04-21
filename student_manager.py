# student_manager.py
from utils import load_data, save_data

def add_student():
    data = load_data()
    try:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {"roll": roll, "name": name, "marks": marks}
        data.append(student)

        save_data(data)
        print("Student added successfully!\n")
    except ValueError:
        print("Invalid input! Please enter correct data.\n")

def view_students():
    data = load_data()
    if not data:
        print("No records found.\n")
        return
    for s in data:
        print(s)

def search_student():
    data = load_data()
    roll = int(input("Enter Roll No to search: "))

    for s in data:
        if s["roll"] == roll:
            print("Student Found:", s)
            return
    print("Student not found!\n")

def update_student():
    data = load_data()
    roll = int(input("Enter Roll No to update: "))

    for s in data:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["marks"] = float(input("Enter new marks: "))
            save_data(data)
            print("Updated successfully!\n")
            return
    print("Student not found!\n")

def delete_student():
    data = load_data()
    roll = int(input("Enter Roll No to delete: "))

    new_data = [s for s in data if s["roll"] != roll]

    if len(data) == len(new_data):
        print("Student not found!\n")
    else:
        save_data(new_data)
        print("Deleted successfully!\n")

def sort_students():
    data = load_data()
    choice = input("Sort by (1) Name (2) Marks: ")

    if choice == "1":
        sorted_data = sorted(data, key=lambda x: x["name"])
    elif choice == "2":
        sorted_data = sorted(data, key=lambda x: x["marks"], reverse=True)
    else:
        print("Invalid choice!\n")
        return

    for s in sorted_data:
        print(s)

def generate_report():
    data = load_data()

    if not data:
        print("No data available.\n")
        return

    topper = max(data, key=lambda x: x["marks"])
    avg = sum(s["marks"] for s in data) / len(data)

    print("===== REPORT =====")
    print("Topper:", topper)
    print("Average Marks:", avg)