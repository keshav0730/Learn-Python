#Palindrome Checker (same forward & backward) :
text = input("Enter a word: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



# Ignore case (so "Madam" works too):
text = input("Enter a word: ").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



# Check full sentence (ignoring spaces):
text = input("Enter a sentence: ").replace(" ", "").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")