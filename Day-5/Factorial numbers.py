def factorial(n):
    """
    This function returns the factorial of a number.
    Factorial of a negative number is not defined.
    """
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def get_factorial_from_user():
    """Reusable function to take input and display factorial"""
    try:
        num = int(input("Enter a number: "))
        result = factorial(num)

        if result is None:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {result}")
    except ValueError:
        print("Please enter a valid integer.")

get_factorial_from_user()

