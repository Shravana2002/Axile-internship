def check_palindrome(text):

    text = text.replace(" ", "").lower()
    
    reversed_text = text[::-1]
    
    if text == reversed_text:
        print("The string is a Palindrome.")
    else:
        print("The string is NOT a Palindrome.")

string = input("Enter a string: ")
check_palindrome(string)
