class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above!")
    else:
        print("Access Granted. You are eligible.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("Program execution completed.")

