"""Coffee machine"""

from os import system, name

LOGO = '''
                 __  __
       ___ ___  / _|/ _| ___  ___
      / __/ _ \| |_| |_ / _ \/ _
     | (_| (_) |  _|  _|  __/  __/
      \___\___/|_| |_|  \___|\___|

        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def main(profit, resources):
    """Run the coffee machine"""
    while True:
        print(LOGO)
        user_input = input(
            'What would you like? (espresso/latte/cappuccino): ').lower()
        if user_input == 'report':
            for k, v in resources.items():
                print(f'{k.title()}: {v}')
            print(f'Money: {profit}')
        if not MENU.get(user_input):
            continue

        required_resource = MENU[user_input]['ingredients']
        not_enough = False
        for k, v in required_resource.items():
            remaining = resources.get(k)
            if remaining < v:
                not_enough = True
                break

        if not_enough:
            print("Sorry there is not enough resources!")
            continue

        print('Please enter coins.')
        quarters = float(input('How many quarters?: ')) * 25
        dimes = float(input('How many dimes?: ')) * 10
        nickles = float(input('How many nickles?: ')) * 5
        pennies = float(input('How many pennies?: '))

        total = (quarters + dimes + nickles + pennies) / 100
        cost = MENU[user_input]["cost"]

        if cost > total:
            print('You did not enter enough money!')
            continue

        change = total - cost
        if change:
            print(f'Here is ${change} in change.')

        print(f'Enjoy your {user_input}')
        for k, v in required_resource.items():
            resources[k] -= v

        profit += cost

    return


def clear():
    """Method to clear the console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main(profit, resources)
