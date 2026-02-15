students = {}

while True:
    print("\n--- Student Dictionary Application ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == '2':
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"Name: {name}, Marks: {marks}")
        else:
            print("No records found.")

    elif choice == '3':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name}'s Marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == '4':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    elif choice == '5':
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

