"""
Simple Calculator Program
Author: David Olawuyi
Description: A menu-driven calculator that performs basic arithmetic operations
"""


def add(Num1, Num2):
    return Num1 + Num2


def subtract(Num1, Num2):
    return Num1 - Num2


def multiply(Num1, Num2):
    return Num1 * Num2


def divide(Num1, Num2):
    if Num2 == 0:
        return "Error: Cannot divide by zero!"
    return Num1 / Num2


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


def get_numbers():
    try:
        Num1 = float(input("Enter the first number: "))
        Num2 = float(input("Enter the second number: "))
        return Num1, Num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None


def main():
    print("Welcome to the simple calculator!")

    while True:
        display_menu()

        try:
            Choice = input("Please select an option (1-5): ").strip()

            if Choice == '5':
                print("\nThank you for using the calculator. Goodbye!")
                break

            elif Choice in ['1', '2', '3', '4']:
                Num1, Num2 = get_numbers()
                if Num1 is None or Num2 is None:
                    continue

                if Choice == '1':
                    Result = add(Num1, Num2)
                    Operation = "Addition"
                    Symbol = '+'

                elif Choice == '2':
                    Result = subtract(Num1, Num2)
                    Operation = "Subtraction"
                    Symbol = '-'

                elif Choice == '3':
                    Result = multiply(Num1, Num2)
                    Operation = "Multiplication"
                    Symbol = '*'

                elif Choice == '4':
                    Result = divide(Num1, Num2)
                    Operation = "Division"
                    Symbol = '/'

                print(f"\n{Operation} Result:")
                print(f"{Num1} {Symbol} {Num2} = {Result}")

                continue_calc = input(
                    "\nWould you like to perform another calculation? (y/n): "
                ).strip().lower()

                if continue_calc not in ['y', 'yes']:
                    print("\nThank you for using the calculator. Goodbye!")
                    break

            else:
                print("Error: Invalid option! Please select a number between 1 and 5.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
