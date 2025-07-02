def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "❌ Cannot divide by zero."

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "❌ Cannot modulus by zero."

def show_menu():
    print("\n🧮 Advanced Python Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("0. Exit")

while True:
    show_menu()
    try:
        choice = int(input("\n🔢 Enter your choice (0 to exit): "))
    except ValueError:
        print("❌ Please enter a valid number from the menu.")
        continue

    if choice == 0:
        print("\n👋 Exiting Calculator. Have a nice day!")
        break

    first = get_number("\nEnter First Number: ")
    second = get_number("Enter Second Number: ")

    if choice == 1:
        print(f"\n✅ Result: {first} + {second} = {add(first, second)}")
    elif choice == 2:
        print(f"\n✅ Result: {first} - {second} = {subtract(first, second)}")
    elif choice == 3:
        print(f"\n✅ Result: {first} * {second} = {multiply(first, second)}")
    elif choice == 4:
        result = divide(first, second)
        print(f"\n✅ Result: {first} / {second} = {result}")
    elif choice == 5:
        result = modulus(first, second)
        print(f"\n✅ Result: {first} % {second} = {result}")
    else:
        print("\n❌ Invalid choice. Please choose from 0 to 5.")
