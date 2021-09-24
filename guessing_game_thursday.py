"""Homework. Advanced level
The Guessing Game
Write a program that generates a random number between
1 and 10 and lets the user guess what number was
generated.
The result should be sent back to the user via a print
statement."""

import random


user_input = input("What number am I thinking of? From 1 to 9 only:  ")


def guessing_game(typed_input):
    guess = random.randint(1, 10)
    typed_input = user_input
    if len(typed_input) > 2:
        print('Please fill in a number from 0 to 10!')
    else:
        try:
            typed_input = int(user_input)
        except ValueError:
            print('Hey, please make sure you type in a number, not letters or something else!')
        else:
            if type(typed_input == int):
                if typed_input <= 10:
                    if guess < typed_input:
                        print(f'It should have been a little lower, it was {str(guess)}.')
                    elif guess > typed_input:
                        print(f'It should have been higher...uf, it was {str(guess)}.')
                    else:
                        print(f'Wow, you guessed it was {str(guess)} unbelievable!')
                else:
                    if typed_input > 10:
                        print('The number is greater than 10, please fill in another!')


if __name__ == '__main__':
    guessing_game(user_input)

