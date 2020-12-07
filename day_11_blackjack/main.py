"""Blackjack Game"""

import random
from os import system, name
from art import LOGO

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
FULL_DECK = CARDS + CARDS + CARDS + CARDS
random.shuffle(FULL_DECK)


def play(number_of_decks, betting_power):
    """Function to play blackjack.

    Args:
        number_of_decks (int): Number of decks to play with
        betting_power (float): How much betting power you have
    """

    decks = shuffle_decks(number_of_decks)
    while True:
        print(LOGO)
        bet = input('Place your bet: ')
        bet = int(bet)
        if bet > betting_power:
            print('You do not have enough chips!')
            continue
        decks, betting_power = play_hand(
            decks, bet, betting_power)
        if len(decks) < 25:
            print('Need to reshuffle the shoe.')
            print(f'You finished with {betting_power} in chips')
            print('###########################################')
            decks = shuffle_decks(number_of_decks)
        play_again = input('Do you want to play another hand (y/n)?: ').lower()
        if play_again == 'n':
            print(f'You finished with {betting_power} in chips')
            return
        else:
            clear()


def shuffle_decks(number_of_decks):
    """Shuffle decks

    Args:
        number_of_decks: (int): number of decks to play with
    Returns:
        list: decks
    """
    decks = []
    for _ in range(0, number_of_decks):
        decks += FULL_DECK

    # shuffle decks
    random.shuffle(decks)
    return decks


def play_hand(decks, bet, betting_power):
    """Play hand

    Args:
        decks (list): List of cards
        bet (int): Number of chips you are wagering
        betting_power (int): How much betting power you have
    Returns:
        tuple: Remaining cards in the deck and betting power
    """
    whos_turn = 'player'
    bet_multiplier = 2.0
    bet_proceeds = 0
    betting_power -= bet
    computer_hand = []
    players_hand = []
    for _ in range(0, 4):
        # Deal cards
        if whos_turn == 'player':
            players_hand.append(decks.pop(0))
            whos_turn = 'computer'
        else:
            computer_hand.append(decks.pop(0))
            whos_turn = 'player'
    print(f'Chips Wagered: {bet} Total chips: {betting_power}')
    print_hands(computer_hand, 'Dealer', dealer_show_one=True)
    print_hands(players_hand, 'Your')
    player_score = calculate_score(players_hand)
    if player_score == 21:
        bet_multiplier = 2.5
        print('Blackjack!!')
    else:
        while True:
            action = input('Do you want to hit stay or double?: ').lower()
            if action == 'hit':
                c = decks.pop(0)
                players_hand.append(c)
                player_score = calculate_score(players_hand)

                # print hands
                clear()
                print(LOGO)
                print(f'Chips Wagered: {bet} Total chips: {betting_power}')
                print_hands(computer_hand, 'Dealer', dealer_show_one=True)
                print_hands(players_hand, 'Your')

                if player_score > 21:
                    print('########## You bust! ##########')
                    return (decks, betting_power)
            elif action == 'double' and len(players_hand) > 2:
                print("You can not double")
                continue
            elif action == 'double':
                double_bet = input('How much do you want to wager: ')
                double_bet = float(double_bet)
                if double_bet > bet:
                    print('You can not wager more than your original bet!')
                    continue
                betting_power -= double_bet
                bet += double_bet
                c = decks.pop(0)
                players_hand.append(c)
                player_score = calculate_score(players_hand)

                # print hands
                clear()
                print(LOGO)
                print(f'Chips Wagered: {bet} Total chips: {betting_power}')
                print_hands(computer_hand, 'Dealer')
                print_hands(players_hand, 'Your')

                if player_score > 21:
                    print('########## You bust! ##########')
                    return (decks, betting_power)
                break
            elif action == 'stay':
                break
            else:
                print('Not a valid option!')

    # Calculate computers score
    computer_score = calculate_score(computer_hand)
    while computer_score < 17:
        c = decks.pop(0)
        computer_hand.append(c)
        computer_score = calculate_score(computer_hand)

        # print hands
        clear()
        print(LOGO)
        print(f'Chips Wagered: {bet} Total chips: {betting_power}')
        print_hands(computer_hand, 'Dealer')
        print_hands(players_hand, 'Your')

    if computer_score > 21:
        betting_power += (bet * bet_multiplier)
        # print hands
        clear()
        print(LOGO)
        print(f'Chips Wagered: {bet} Total chips: {betting_power}')
        print_hands(computer_hand, 'Dealer')
        print_hands(players_hand, 'Your')
        print('########## Dealer bust, you win! ##########')
        return (decks, betting_power)

    if computer_score > player_score:
        # print hands
        clear()
        print(LOGO)
        print(f'Chips Wagered: {bet} Total chips: {betting_power}')
        print_hands(computer_hand, 'Dealer')
        print_hands(players_hand, 'Your')
        print(f'########## You lose. Dealer - {computer_score} You - {player_score} ##########')  # noqa
    elif computer_score < player_score:
        # print hands
        clear()
        print(LOGO)
        print(f'Chips Wagered: {bet} Total chips: {betting_power}')
        print_hands(computer_hand, 'Dealer')
        print_hands(players_hand, 'Your')
        bet_proceeds = bet * bet_multiplier
        print(f'########## You Win. Dealer - {computer_score} You - {player_score} ##########')  # noqa
    else:
        # print hands
        clear()
        print(LOGO)
        print(f'Chips Wagered: {bet} Total chips: {betting_power}')
        print_hands(computer_hand, 'Dealer')
        print_hands(players_hand, 'Your')
        bet_proceeds = bet
        print(f'########## Tie. Dealer - {computer_score} You - {player_score} ##########')  # noqa

    betting_power += bet_proceeds
    return (decks, betting_power)


def calculate_score(hand):
    """Calculate score of a hand.

    Face cards (J, K, Q) equal 10

    Args:
        hand (list): list of cards
    Returns:
        int: score of hand
    """
    score = 0
    # Move the A to the end
    if 'A' in hand:
        hand.pop(hand.index('A'))
        hand.append('A')

    for card in hand:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            if (score + 11) > 21:
                score += 1
            else:
                score += 11
        else:
            score += int(card)
    return score


def print_hands(hand, player_name, dealer_show_one=False):
    """Print the hand of a player

    Args:
        hand (list): list of cards
        player_name (str): Name of the player
        dealer_show_one (bool): If you only want the dealer to show one card
    """
    if dealer_show_one:
        temp = [hand[0]]
        score = calculate_score(temp)
        print(f'{player_name} Showing - {score}')
    else:
        score = calculate_score(hand)
        print(f'{player_name} Hand - {score}')

    lines = [[] for i in range(0, 6)]
    cards = [str(c) for c in hand]
    lines[0].append('.--------.' * len(cards))

    top_number = ''
    for idx, c in enumerate(cards):
        if dealer_show_one and idx > 0:
            c = ' '
        space = ''
        if len(c) == 1:
            space = ' '
        r = '|{}{} /\   |'.format(c, space)
        top_number += r
    lines[1].append(top_number)

    lines[2].append('|  /  \  |' * len(cards))
    lines[3].append('|  \  /  |' * len(cards))

    bottom_number = ''
    for idx, c in enumerate(cards):
        if dealer_show_one and idx > 0:
            c = ' '
        space = ''
        if len(c) == 1:
            space = ' '
        r = '|   \/ {}{}|'.format(c, space)
        bottom_number += r
    lines[4].append(bottom_number)
    lines[5].append('`--------`' * len(cards))

    for line in lines:
        print(''.join(line))


def clear():
    """Method to clear the console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == "__main__":
    play(5, 100.00)
