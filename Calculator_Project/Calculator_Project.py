"""
Simple Calculator Program
Author: David Olawuyi
Description: A menu-driven calculator that performs basic arithmetic operations
"""

# Arithmetic functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

# Display menu
def display_menu():
    print("\n" + "=" * 40)
    print("     SIMPLE CALCULATOR")
    print("=" * 40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 40)

# Get user numbers
def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

# Main program
def main():
    print("Welcome to the Simple Calculator!")

    while True:
        display_menu()
        choice = input("Please select an option (1-5): ").strip()

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()

            if num1 is None or num2 is None:
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
                symbol = '+'

            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
                symbol = '-'

            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
                symbol = '*'

            elif choice == '4':
                result = divide(num1, num2)
                operation = "Division"
                symbol = '/'

            print(f"\n{operation} Result:")
            print(f"{num1} {symbol} {num2} = {result}")

            again = input("\nDo you want to calculate again? (y/n): ").strip().lower()
            if again not in ['y', 'yes']:
                print("\nThank you for using the calculator. Goodbye!")
                break

        else:
            print("Error: Invalid option! Please select between 1 and 5.")
if __name__ == "__main__":
    main()