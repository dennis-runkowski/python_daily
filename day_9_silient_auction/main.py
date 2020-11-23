"""Silient Auction App"""
from os import system, name

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def main():
    """Silient Auction method"""
    print(logo)
    print('Welcome to the silient auction.')
    data = {}
    while True:
        name = input('What is your name?: ')
        bid = input('What is your bid?: ')
        data[name] = bid
        more = input('Are there any other bidders? (yes or no): ')
        clear()
        if more == 'no':
            break
    print("############################################################")
    print(logo)
    winner = max(data, key=data.get)
    print(f'                     The winner is {winner}!')
    print("############################################################")


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
