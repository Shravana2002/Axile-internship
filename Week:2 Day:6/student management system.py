students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student = {
        "Roll": roll,
        "Name": name,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")

def display_students():
    if len(students) == 0:
        print("No student records found!\n")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print("Roll:", student["Roll"])
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            print("----------------------")
        print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found!")
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            found = True
            break

    if not found:
        print("Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Please try again.\n")

