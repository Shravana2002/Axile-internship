def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition =", a + b)

def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

def check_prime():
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Not a Prime Number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")

def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial =", fact)

def reverse_string():
    text = input("Enter a string: ")
    print("Reversed String =", text[::-1])


while True:
    print("\n===== MENU =====")
    print("1. Addition of Two Numbers")
    print("2. Check Even or Odd")
    print("3. Check Prime Number")
    print("4. Find Factorial")
    print("5. Reverse a String")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add()
    elif choice == 2:
        check_even_odd()
    elif choice == 3:
        check_prime()
    elif choice == 4:
        factorial()
    elif choice == 5:
        reverse_string()
    elif choice == 6:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Please select a valid option.")

