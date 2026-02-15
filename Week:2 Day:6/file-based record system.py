FILENAME = "student_records.txt"

def add_record():
    with open(FILENAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        file.write(roll + "," + name + "," + marks + "\n")
    print("Record Added Successfully!\n")

def view_records():
    try:
        with open(FILENAME, "r") as file:
            print("\n--- Student Records ---")
            for line in file:
                roll, name, marks = line.strip().split(",")
                print(f"Roll No: {roll}, Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("No records found!\n")

def search_record():
    roll_search = input("Enter Roll Number to Search: ")
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                if roll == roll_search:
                    print(f"Record Found → Name: {name}, Marks: {marks}")
                    found = True
                    break
        if not found:
            print("Record Not Found!")
    except FileNotFoundError:
        print("No records found!\n")

while True:
    print("\n--- File Based Record System ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.")

