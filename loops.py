# QS1 -> print numbers from 1 to 100.
i = 1                #initialization
while i <= 100:      #stopping condition
    print(i)
    i += 1

# QS2 -> print numbers from 100 to 1.abs
i = 100
while i >= 1:
    print(i)
    i -= 1

# QS3 -> print multiplication table of a number n.
n = int(input("enter a number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1 

# QS4 -> printnthe elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])  #...print(nums[9]) or print(nums[len(nums)-1])  # This is for printing manually one by one

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])   # nums[0], nums[1], nums[2]...
    idx += 1

heroes = ["ironman", "thor", "batman", "spiderman", "superman"]
idx = 0                          # note: # traverse -> means travelling on words one by one
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

# QS5 -> Search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)

x = 64

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
    else:
        print("Finding...")   
    i += 1

