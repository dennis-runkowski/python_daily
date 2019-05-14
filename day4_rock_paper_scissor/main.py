"""
Rock Paper Scissors Game
"""
import random

options = [
    "rock",
    "paper",
    "scissors"
]

# Key beats value
winner_table = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def get_computer_choice():
    """
    Randomly select option

    Returns:
        str with rock, paper or scissors
    """
    choice = random.randint(0, 2)
    decision = options[choice]
    return decision

def get_winner(player_1, computer):
    """
    Determine if the computer is the winner.
    Args:
        player_1 (str): player one choice
        computer (str): computer choice

    Returns:
        str with the decision tie, win or lose
    """
    if player_1 == computer:
        return "It is a tie!"

    if winner_table.get(computer, "") == player_1:
        return "Computer wins."
    else:
        return "You win!"


if __name__ == "__main__":
    print("#######################################################")
    print("#######################################################")
    print("#######################################################")
    print("##############|                         |##############")
    print("##############| Rock - Paper - Scissors |##############")
    print("##############|_________________________|##############")
    print("#######################################################")
    print("#######################################################")
    print("#######################################################")

    run_game = True
    while run_game:
        player = input("Please enter rock, paper or scissors: ")
        player = player.lower()
        if player not in options:
            print("Please enter a valid option!")
        else:
            computer = get_computer_choice()
            decision = get_winner(player, computer)
            print("{p} ---> {c}".format(p=player, c=computer))
            print(decision)
        print("         ")
        play_again = input("Do you want to play again (y/n)? ")
        print("   ")
        play_again = play_again.lower()
        if play_again != "y":
            run_game = False
