# lab 6 encoder Karina Ann

def encode(password):
    # create list out of string passcode
    password_list = list(password)

    # iterate through each item in list and add 3
    for index, item in enumerate(password_list):
        password_list[index] = int(item) + 3

    # turn password_list back into a string using final
    final = ''

    # iterate though each item in list and turn into string
    for index, item in enumerate(password_list):
        final = final + str(password_list[index])

    return final


def decode(encoded):  # Michael Amiot
    decoded = ''
    password_list = list(encoded)
    # iterate through each item in password_list and subtract 3
    for index, item in enumerate(password_list):
        password_list[index] = int(item) - 3
        decoded += str(password_list[index])
    return f'The encoded password is {encoded}, and the original password is {decoded}'


if __name__ == '__main__':

    print("Encoder/Decoder Menu\n--------\n1. Encode\n2. Decode\n3. Quit")
    menu_option = int(input("\nSelect a Menu Option: "))

    while True:
        if menu_option == 1:
            passcode = str(input("\nEnter password to encode: "))
            print(f'Your password has been encoded and stored!')
            stored = encode(passcode)
            print("\nEncoder/Decoder Menu\n--------\n1. Encode\n2. Decode\n3. Quit")
            menu_option = int(input("\nSelect a Menu Option: "))
            print()

        if menu_option == 2:  # Michael Amiot Decode option
            print(decode(stored))
            print("\nEncoder/Decoder Menu\n--------\n1. Encode\n2. Decode\n3. Quit")
            menu_option = int(input("\nSelect a Menu Option: "))
            print()

        if menu_option == 3:
            print("Goodbye!")
            quit()
