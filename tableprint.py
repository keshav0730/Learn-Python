# Print Mutiplication Table 
# nums = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#     print(f"{nums} x {i} = {nums * i}")

# For example print multiplication table of 2 enter 2 and run the code same as for 3,4,5,etc.
# Output:
# Enter a number to print its multiplication table: 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

# Print 2 multiplication table at same time.
# num = int(input("Enter a number to print 2 multiplication table at same time: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i} \t {num + 1} x {i} = {(num + 1) * i}")

# Output:
# Enter a number to print 2 multiplication table at same time: 2
# 2 x 1 = 2 	 3 x 1 = 3
# 2 x 2 = 4 	 3 x 2 = 6
# 2 x 3 = 6 	 3 x 3 = 9
# 2 x 4 = 8 	 3 x 4 = 12
# 2 x 5 = 10 	 3 x 5 = 15
# 2 x 6 = 12 	 3 x 6 = 18
# 2 x 7 = 14 	 3 x 7 = 21
# 2 x 8 = 16 	 3 x 8 = 24
# 2 x 9 = 18 	 3 x 9 = 27
# 2 x 10 = 20 	 3 x 10 = 30
# Print multiplication table of 2 to 10 at same time.
for num in range(1, 11):
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
# Output:
# Multiplication Table of 2:
# 2 x 1 = 2
# 2 x 2 = 4
#to print table of 2 to 10: