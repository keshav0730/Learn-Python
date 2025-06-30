# This code counts the number of vowels in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string is: {count}")

# Output: 
# Enter a string: Hey there i am using VScode for Python
# The number of vowels in the string is: 11



# This code counts and found the number of vowels in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
found = ""

for char in text:
    if char in vowels:
        count += 1
        found += char

print(f"The number of vowels in the string is: {count}")
print(f"The vowels found in the string are: {found.strip()}")
# Output:
# Enter a string: Hey whatsup buddy
# The number of vowels in the string is: 4
# The vowels found in the string are: e a u u
