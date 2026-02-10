numbers = [45, 12, 89, 23, 67, 2, 90]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("List of numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
