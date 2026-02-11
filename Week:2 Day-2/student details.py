student = {
    "name": "Shravana Naik",
    "roll_number": 77,
    "class": "MCA Grade",
    "section": "A",
    "age": 23,
    "gender": "Female",
    "marks": {
        "Math": 88,
        "Python": 92,
        "English": 85
    }
}

print("Student Details:")
print("Name:", student["name"])
print("Roll Number:", student["roll_number"])
print("Class:", student["class"])
print("Section:", student["section"])
print("Age:", student["age"])
print("Gender:", student["gender"])

print("\nMarks:")
for subject, score in student["marks"].items():
    print(subject, ":", score)

