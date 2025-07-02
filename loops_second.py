#show All The Number Between Given Number

first_number=int(input("Please Enter First Number: "))
last_number=int(input("Please Enter Last Number: "))

if(last_number>first_number):
     for num in  range (first_number+1,last_number):
      print(num)
elif(first_number>last_number):
   for num in range(first_number-1,last_number,-1):
      print(num)
else:
   print("Both Number are Equals")
    


# Print 1 to N 
# Input a number N from the user and print all numbers from 1 to N.

number=int(input("Please Enter Your Number:"))

for num in range(1,number):
    print(num)

#add All the Numbers in between number given by user from 1

num=int(input("Please Enter Your Number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)
