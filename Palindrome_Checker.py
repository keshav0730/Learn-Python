#Palindrome Checker (same forward & backward)
text = input("Enter a word: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

