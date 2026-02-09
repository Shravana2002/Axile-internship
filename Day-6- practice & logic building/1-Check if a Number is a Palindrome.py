def is_palindrome(num):
    original = str(num)
    return original == original[::-1]

n = int(input("Enter a number: "))
if is_palindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome")

