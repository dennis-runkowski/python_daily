"""Play Rock Paper Scissors. """

import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
MAP = {
    "rock": ROCK,
    "paper": PAPER,
    "scissors": SCISSORS
}
VALID_TYPES = ["rock", "paper", "scissors"]


def main():
    """Main method for the game."""
    print("#####################################")
    print("   Lets Play Rock, Paper, Scissors   ")
    print("#####################################")

    play_again = True
    while play_again:
        user = input("What do you choose? Type Rock, Paper or Scissors:\n")
        user = user.lower()
        if user not in VALID_TYPES:
            print("Please pick a valid option.")
            continue
        print(MAP[user])
        computer = random.randint(0, 2)
        computer = VALID_TYPES[computer]
        print(f"Computer choose {computer}")
        print(MAP[computer])
        print("")
        if user == computer:
            print("Draw!")
        elif user == "rock" and computer == "scissors":
            print("You Win!")
        elif user == "paper" and computer == "rock":
            print("You Win!")
        elif user == "scissors" and computer == "paper":
            print("You Win!")
        elif computer == "rock" and user == "scissors":
            print("You Lose!")
        elif computer == "paper" and user == "rock":
            print("You Lose!")
        elif computer == "scissors" and user == "paper":
            print("You Lose!")

        keep_playing = input("Do you want to play again (yes or no)? ").lower()
        if keep_playing == "no":
            play_again = False


if __name__ == "__main__":
    main()
