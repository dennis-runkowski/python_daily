"""Guess the number game."""

import random

DIFF = {
    'easy': 10,
    'hard': 5
}


def main(difficulty):
    """Run the game.

    Args:
        difficulty (str): difficulty for the game
    """
    print('Welcome to the guessing game!')
    print('I am thinking of a number between 1 and 100.')
    number = random.randint(1, 100)
    if difficulty not in DIFF:
        print("Defaulting difficulty to easy....")
        guesses = 10

    guesses = DIFF[difficulty]

    while True:
        if guesses < 1:
            print('You have no more guesses. You lose :(')
            return
        print(f'You have {guesses} attempts remaining to guess the number.')
        guesses -= 1
        guess = int(input("Make a guess: "))

        if guess == number:
            print('You guessed the number! You Won :)')
            return

        if guess > number:
            print('Too high.')
        else:
            print('Too low.')
        print('')

    return


if __name__ == "__main__":
    user_diff = input('Choose a difficulty. Type easy or hard: ').lower()
    main(user_diff)
