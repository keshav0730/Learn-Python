# Find the smallest number in a list.
a = float(input("Enter the first number: "))   # float for decimal support
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a <= b and a <= c:
    print("The smallest number is:", a)
elif b <= a and b <= c:
    print("The smallest number is:", b)
else:
    print("The smallest number is:", c)
# This code takes three numbers as input and prints the smallest one.
# It uses a series of conditional statements to compare the numbers.

# Output:
# Enter the first number: 5
# Enter the second number: 3
# Enter the third number: 8
# The smallest number is: 3.0
    