"""OOP Coffee Machine"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def main():
    """Main function to run"""
    while True:
        drinks = menu.get_items()
        user_input = input(f'What would you like to drink {drinks}?: ')

        if user_input == 'report':
            coffee_maker.report()
            money_machine.report()
            continue

        check_drink = menu.find_drink(user_input)
        if not check_drink:
            continue
        if not coffee_maker.is_resource_sufficient(check_drink):
            continue
        if not money_machine.make_payment(check_drink.cost):
            continue

        coffee_maker.make_coffee(check_drink)



if __name__ == "__main__":
    main()
