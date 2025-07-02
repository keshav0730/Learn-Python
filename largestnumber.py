# Find Largest of 3 Numbers using if-elif-else conditions.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

# Output: Largest number is: <largest number>
# Enter first number: 30
# Enter second number: 50
# Enter third number: 70
# Largest is: 70



# Find Largest of 3 Numbers using max() function.
largest = max(a, b, c)
print("Largest is:", largest)
# Output: Largest number is: <largest number>
# Enter first number: 30
# Enter second number: 50
# Enter third number: 70
# Largest is: 70

