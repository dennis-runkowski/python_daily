"""Calculator App"""

from os import system, name

logo = logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def main(a, b, op):
    """Main calculator function
    Args:
        a (float): First number
        b (float): Second number
        op (str): Type of operation
    Returns:
        float: result of operation
    """
    my_funct = OPERATION.get(op)
    if not my_funct:
        return "Please use a valid operation!"

    result = my_funct(a, b)
    return result


def add(a, b):
    """Add two float together.

    Args:
        a (float): First number to add
        b (float): Second number to add
    Returns:
        float: Sum of two numbers
    """
    return a + b


def subtract(a, b):
    """Subtract two float.

    Args:
        a (float): First number to subtract
        b (float): Second number to subtract
    Returns:
        float: Difference of two numbers
    """
    return a - b


def multiply(a, b):
    """Multiply two float together.

    Args:
        a (float): First number to multiply
        b (float): Second number to multiply
    Returns:
        float: Product of two numbers
    """
    return a * b


def divide(a, b):
    """Divide two float together.

    Args:
        a (float): First number to divide
        b (float): Second number to divide
    Returns:
        float: Division of two numbers
    """
    return a / b


def clear():
    """Method to clear the console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


OPERATION = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

if __name__ == "__main__":
    print(logo)
    while True:
        num1 = float(input("What's the first number?: "))
        num2 = float(input("What's the second number?: "))
        symbols = " ,".join([x for x in OPERATION])
        op = input(f"Pick one of the following operations ({symbols}): ")
        result = main(num1, num2, op)
        print(f"The result is: {result}")
        cont = input("Do you want to perform another operation (yes or no)?: ")
        if cont == "yes":
            clear()
        else:
            break
