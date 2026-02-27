from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Show form
@app.route("/")
def form():
    return render_template("form.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                   (name, email, course))
    conn.commit()
    conn.close()

    return redirect("/display")

# Display stored data
@app.route("/display")
def display():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return render_template("display.html", students=data)

if __name__ == "__main__":
    app.run(debug=True)
