# Show all the numbers between two given numbers
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))

if first_num < second_num:
    for i in range(first_num + 1, second_num):
        print(i)
else:
    for i in range(second_num + 1, first_num):
        print(i)
print("Done!")
# This code will print all the numbers between two given numbers, excluding the numbers themselves.
# If the first number is greater than the second, it will still work correctly.



# Show all the number between given number 
first_number = int(input("Please enter first number: "))
last_number = int(input("Please enter last number: "))

if (last_number > first_number):
    for num in range (first_number + 1, last_number):
        print(num)
elif (first_number > last_number):
    for num in range (first_number - 1, last_number):
        print(num)
else:
    print("Both numbers are equal, no numbers in between.")


    