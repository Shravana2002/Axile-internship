import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")

def insert_student():
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
                   (name, course, marks))
    conn.commit()
    print("Record Inserted Successfully")

def fetch_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\nStudent Records:")
    for row in records:
        print(row)

def update_student():
    id = int(input("Enter ID to Update: "))
    marks = int(input("Enter New Marks: "))
    cursor.execute("UPDATE students SET marks=? WHERE id=?", (marks, id))
    conn.commit()
    print("Record Updated Successfully")

def delete_student():
    id = int(input("Enter ID to Delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Record Deleted Successfully")


while True:
    print("\n1. Insert")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        insert_student()
    elif choice == '2':
        fetch_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid Choice")

conn.close()
