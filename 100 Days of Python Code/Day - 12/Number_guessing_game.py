#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import sys
from art import logo

guess_number = random.randint(1, 101)
print(logo)
print("Welcome to number Guessing Game!!")
print("I'm thinking of a number between 1 to 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    count = 10
elif level == 'hard':
    count = 5
else:
    print("Invalid input")
    sys.exit()


def game():
    global count
    global guess_number
    while count > 0:
        print(f"You have {count} no of guesses left")
        guess = int(input("Enter a guess: "))
        if guess > guess_number:
            print("Too High")
            if count > 1:
                print("Guess again")
            count -= 1
        elif guess < guess_number:
            print("Too Low")
            if count > 1:
                print("Guess again")
            count -= 1
        else:
            print(f"The number is {guess}")
            print("You made the right guess")
            return True


result = game()
if result != True:
    print(f"The number was {guess_number}")
