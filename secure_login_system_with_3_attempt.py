# secure login system with 3 attempts — this is a real-world concept used in many applications.
import getpass

for i in range(3):
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if username == "admin" and password == "pass123":
        print("Login successful!")
        break
    else:
        print("Login failed. Please try again.\n")

else:
    print("Too many attempts. Access denied.")

# This code allows a user to attempt to log in up to three times.

# Sample Run:
# Enter your username: admin
# Enter your password: 
# Login successful!

# OR

# Login failed. Please try again.
# Login failed. Please try again.
# Too many attempts. Access denied.


        

