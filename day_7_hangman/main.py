"""Hangman Game"""
import random
from word_list import WORD_LIST
from stages import STAGES


def main():
    """Hangman"""
    print(''' 
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    
    ''')

    chosen_word = random.choice(WORD_LIST)
    chosen_list = ["_" for i in chosen_word]

    stages = STAGES
    lives = len(stages)
    print(f"You have {lives} lives!")
    print(" ".join(chosen_list))

    game = True
    guesses = []
    while game:
        print("")

        guess = input("Guess a letter: ").lower()
        if guess in guesses:
            print(f"You already guessed {guess}")
            continue

        guesses.append(guess)

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print("Game Over. You Lose!")
                print(STAGES[lives])
                return
            else:
                print("Letter not in word")

            print(STAGES[lives])

        for idx, letter in enumerate(chosen_word):
            if guess == letter:
                chosen_list[idx] = letter

        print(" ".join(chosen_list))


if __name__ == "__main__":
    main()
