"""Password Generator"""

import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # noqa
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def main():
    """Generate password function"""
    print("#####################################")
    print("         Password Generator          ")
    print("""

            .--------
          / .------. \ 
         / /        \ \ 
         | |        | |
        _| |________| |_
      .' |_|        |_| '.
      '._____ ____ _____.'
      |     .'____'.     |
      '.__.'.'    '.'.__.'
      '.__  |      |  __.'
      |   '.'.____.'.'   |
      '.____'.____.'____.'
      '.________________.'             
    """)
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input(
        "How many letters would you like in your password?\n")
    )
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    generate_l = [random.randint(0, 51) for i in range(0, nr_letters)]
    generate_l = [LETTERS[i] for i in generate_l]

    generate_s = [random.randint(0, 8) for i in range(0, nr_symbols)]
    generate_s = [SYMBOLS[i] for i in generate_s]

    generate_n = [random.randint(0, 9) for i in range(0, nr_numbers)]
    generate_n = [NUMBERS[i] for i in generate_n]

    password = generate_l + generate_n + generate_s
    random.shuffle(password)
    password = "".join(password)
    print("Please see your new password below:")
    print("")
    print(password)
    print("")
    print("#####################################")


if __name__ == "__main__":
    main()
