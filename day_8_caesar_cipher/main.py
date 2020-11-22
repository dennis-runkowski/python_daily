"""Caesar Cipher encoder"""


LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # noqa


def cipher(text, shift, cipher_type):
    """ text using the caesar cipher

    Args:
        text (str): Text to encrypt
        shift (int): Shift used for the cipher
        cipher_type (str): read or write

    Return:
        str: encoded message
    """
    if shift > 25:
        return 'Shift must be between 0 and 26'

    if cipher_type == 'read':
        LETTERS.reverse()

    cipher_list = []
    for letter in text:
        if letter in LETTERS:
            position = LETTERS.index(letter) + shift
            if position > 25:
                position = position - 26
            letter = LETTERS[position]
        cipher_list.append(letter)
    return "".join(cipher_list)


if __name__ == "__main__":
    print('''
            _       _               
            (_)    | |              
        ___ _ _ __ | |__   ___ _ __ 
        / __| | '_ \| '_ \ / _ \ '__|
        | (__| | |_) | | | |  __/ |   
        \___|_| .__/|_| |_|\___|_|   
            | |                    
            |_|
    ''')
    print("Use cltr c to break out of the convo!")
    shift = int(input("What shift are you using? "))
    while True:
        read_write = input("Do you want to read or write a message (r/w)? ")
        read_write = read_write.lower()
        text = input("Please input the text\n").lower()
        print("")
        print("#########################################################")
        if read_write == 'r':
            output = cipher(text, shift, 'read')
        elif read_write == 'w':
            output = cipher(text, shift, 'write')
        else:
            print("Please use r for read and w for write!")

        print(output)
        print("#########################################################")
