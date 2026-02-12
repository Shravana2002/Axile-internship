text = input("Enter a string: ")

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("\nCharacter Frequency:")
for key, value in freq.items():
    print(f"'{key}' : {value}")

print("\nString Operations:")

print("Length of string:", len(text))

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

print("Reversed string:", text[::-1])

if text == text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

print("String without spaces:", text.replace(" ", ""))

words = text.split()
print("Number of words:", len(words))
