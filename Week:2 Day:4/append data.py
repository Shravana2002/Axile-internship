file = open("sample.txt", "a")

data = input("Enter the text to append: ")

file.write(data + "\n")

file.close()

print("Data appended successfully!")
