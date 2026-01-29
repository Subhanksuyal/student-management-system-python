def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    with open("student_data.txt", "a") as f:
        f.write(f"{roll},{name},{marks},{grade}\n")

    print("Student added successfully")


def view_students():
    try:
        with open("student_data.txt", "r") as f:
            for line in f:
                roll, name, marks, grade = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}, Grade: {grade}")
    except FileNotFoundError:
        print("No data found")


def search_student():
    search_roll = input("Enter roll number to search: ")
    found = False

    with open("student_data.txt", "r") as f:
        for line in f:
            roll, name, marks, grade = line.strip().split(",")
            if roll == search_roll:
                print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
                found = True
                break

    if not found:
        print("Student not found")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
