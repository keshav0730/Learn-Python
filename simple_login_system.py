# a simple login system using if conditions in Python — this is a classic mini-project for beginners.
username = input("Enter your username: ")
password = input("Enter your password: ")
# Predefined credentials
correct_username = "admin"
correct_password = "password@123"
# Check if the entered credentials match the predefined ones
if username == "admin" and password == "password@123":
    print("Login successfully!")
else:
    print("Invalid Credentials.")
# This code checks if the entered username and password match the predefined credentials.
# If they match, it prints a success message; otherwise, it prints an error message.

# Output: 
# This is for a successful login
# Enter your username: admin
# Enter your password: password@123
# Login successfully!

# This is for an unsuccessful login
# Enter your username: user
# Enter your password: wrongpassword
# Invalid Credentials.
