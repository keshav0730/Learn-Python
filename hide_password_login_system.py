# Hide password input (for better privacy):
import getpass
username = input("Enter the username: ")
password = getpass.getpass("Enter the password: ")
# Simulate a login system
if username == "admin" and password == "secret":
    print("Login successful!")
else:
    print("Login failed! Incorrect username or password.")  
      
# Note: The getpass module is used to hide the password input in the terminal.
# This is useful for command-line applications where you want to keep the password hidden.

# Example: 
# This code is for correct login credentials:
# Enter the username: admin
# Enter the password:
# Login successful!

# This code is for incorrect login credentials:
# Enter the username: admin
# Enter the password:
# Login failed! Incorrect username or password.

# In this example, the password input is hidden, enhancing privacy during login.
