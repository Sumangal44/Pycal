def create_calculator_banner():
    banner = """
     
██████╗░██╗░░░██╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝░╚████╔╝░██║░░╚═╝███████║██║░░░░░
██╔═══╝░░░╚██╔╝░░██║░░██╗██╔══██║██║░░░░░
██║░░░░░░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
    """
    print(banner)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

# Call the function to display the calculator banner
create_calculator_banner()

# Main calculator loop
while True:
    print("[Select operation:]")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")

    print()  # Print a blank line for better readability
    

