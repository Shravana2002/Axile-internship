def add_student():
    file = open("students.txt", "a")  
    
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    marks = input("Enter Marks: ")
    
    file.write(f"Name: {name}, Roll No: {roll}, Marks: {marks}\n")
    file.close()
    
    print("Student record added successfully!\n")


def display_students():
    try:
        file = open("students.txt", "r")   
        print("\n--- Student Records ---")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No records found. File does not exist.\n")
while True:
    print("1. Add Student Record")
    print("2. Display Student Records")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")

