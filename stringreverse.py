# Print the reverse of a string with a step of 1
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed:", reversed_text)

# Output:
# Enter a string: Hey There!
# Reversed: !erehT yeH



# Print the reverse of a string with a step of like 2, # i.e. every second character
text = input("Enter a string: ")
reversed_text_step2 = text[::-2]
print("reversed with step 2:", reversed_text_step2)

# Output:
# Enter a string: How are you?
# reversed with step 2: ?o r o    



# Equivalent logic using a loop: If you didn’t use slicing, this is how you could reverse a string manually:
text = "hello there"
reversed_text_manual = ""
for char in text:
    reversed_text_manual = char + reversed_text_manual
print("Reversed manually:", reversed_text_manual)

# Output:
# Reversed manually: ereht olleh



# Equivalent logic using a loop with step 2:
text = "What are Your Doing?"
reversed_text = ""

# Start from the last index and go backward with step -2
i = len(text) - 1  # start from last character

while i >= 0:
    reversed_text += text[i]
    i -= 2  # skip one character each time

print("Reversed with step -2:", reversed_text)

# Output:
# Reversed with step -2: ?no uYeath
# Note: The output will vary based on the input string.
# The output will show every second character in reverse order.


