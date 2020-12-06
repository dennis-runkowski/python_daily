"""Doc String"""

from os import system, name
from art import vs, logo
from data import data
import random


def main():
    """Higher lower game"""
    score = 0
    random.shuffle(data)
    compare = 0
    guess_store = {
        'guess_a': 0,
        'guess_b': 0
    }
    print(logo)
    print('Current score: 0!')
    for item in data:

        compare += 1
        if compare == 2:
            compare = 0
            guess_store['guess_b'] = item['follower_count']
            print(vs)
            print(
                f'Against B: {item["name"]}, a {item["description"]}'
                f' from {item["country"]}'
            )
            guess = input('Who has more followers: Type A or B: ').lower()
            guess = f'guess_{guess}'
            winner = max(guess_store, key=(lambda k: guess_store[k]))
            if guess == winner:
                score += 1
                clear()
                print(logo)
                print(f'You are correct! Current score: {score}!')
                continue
            else:
                print(f'You are wrong. Game Over. Score: {score}')
                return

        guess_store['guess_a'] = item['follower_count']
        print(
            f'Compare A: {item["name"]}, a {item["description"]}'
            f' from {item["country"]}'
        )


def clear():
    """Method to clear the console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()

