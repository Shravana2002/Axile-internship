def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number is:", find_largest(nums))
