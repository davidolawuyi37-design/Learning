"""
Number Guessing Game
Author:  David Olawuyi
Description: A number guessing game with difficulty levels, attempt counter and input validation.
"""

import random
print("Welcome To The Number Guessing Game!")

# Difficulty Selection
print("\nChoose A Difficulty Level:")
print("1. Easy (1 - 10)")
print("2. Medium (1 - 20)")
print("3. Hard (1 - 50)")

while True:
    Level = input("Enter 1, 2, or 3: ")

    if Level == "1":
        Max_Number = 10
        break
    elif Level == "2":
        Max_Number = 20
        break
    elif Level == "3":
        Max_Number = 50
        break
    else:
        print("Invalid Choice. Please choose 1, 2, or 3.")

# Generate Random Number
Secret_Number = random.randint(1, Max_Number)
Attempts = 0

print(f"\nYou have choosen a number between 1 and {Max_Number}.")
print("Start Guessing!\n")

# Game Loop
while True:
    Guess = input("Enter your guess: ")

    if not Guess.isdigit():
        print("Please, enter a valid number.\n")
        continue

    Guess = int(Guess)
    Attempts += 1

    if Guess > Secret_Number:
        print("Too high! Try again.\n")
    elif Guess < Secret_Number:
        print("Too Low! Try again.\n")
    else:
        print(
            f"Congratulations! You guessed the number in {Attempts} Attempts.")
        break
