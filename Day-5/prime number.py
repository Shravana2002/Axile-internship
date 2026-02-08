def is_prime(number):
    """Return True if number is prime, otherwise False."""
    
    if number <= 1:
        return False  
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  
    
    return True  


def check_prime():
    """Take input from user and check if it is prime."""
    
    num = int(input("Enter a number: "))
    
    if is_prime(num):
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is NOT a Prime Number.")


check_prime()

