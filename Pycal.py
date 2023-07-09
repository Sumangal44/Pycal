def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user for the operation
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice of operation
choice = input("Enter the operation number (1-4): ")

# Perform the selected operation
if choice == "1":
    result = add(num1, num2)
    operator = "+"
elif choice == "2":
    result = subtract(num1, num2)
    operator = "-"
elif choice == "3":
    result = multiply(num1, num2)
    operator = "*"
elif choice == "4":
    result = divide(num1, num2)
    operator = "/"
else:
    print("Invalid choice")
    exit()

# Display the result
print(f"{num1} {operator} {num2} = {result}")

