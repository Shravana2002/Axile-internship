def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

number = int(input("Enter a number: "))
if is_armstrong(number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
