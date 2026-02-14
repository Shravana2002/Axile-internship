try:
    file = open("student.txt", "r")
    content = file.read()
    print("File Content:\n")
    print(content)
    
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You don't have permission to access this file.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("\nProgram completed.")

