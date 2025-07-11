num = input("Enter a number: ")
sum_of_digits = 0
for digit in num:
    sum_of_digits += int(digit)
print("The sum of the digits is:", sum_of_digits)
 # This code takes a number as input and calculates the sum of its digits.
# It iterates through each character in the string representation of the number,
# converts it to an integer, and adds it to the total sum.
# The final result is printed to the console.

# Output :
# Example: If the input is "123", the output will be "The sum of the
# digits is: 6".
