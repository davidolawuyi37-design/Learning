"""
Number Guessing Game
Author: David Olawuyi
Description: A simple game where the user guesses a randomly generated number.
"""

import random
# Generate a random number between 1 and 10
Secret_Number = random.randint(1, 10)

print("Welcome To The Number Guessing Game!")
print("I have chosen a number between 1 and 10.")
print("Try to guess it!\n")

#Loop until the correct number is guessed
while True:
    Guess = int(input("Enter your guess: "))

    if Guess > Secret_Number:
        print("Too high! Try again.\n")
    elif Guess < Secret_Number:
        print("Too low! Try again.\n")
    else:
        print("Congratulations! You guessed the correct number!")
        break