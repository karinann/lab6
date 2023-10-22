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


while True:
    print("Encoder/Decoder Menu\n--------\n1. Encode\n2. Decode\n3. Quit")

    menu_option = int(input("\nPlease enter an option: "))

    while True:
        if menu_option == 1:
            passcode = str(input("Please enter your password to encode: "))
            stored = encode(passcode)
            print("Your password has been encoded and stored!")

    menu_option = int(input("\nPlease enter an option: "))

    while True:
        if menu_option == 1:
            passcode = str(input("\nEnter password to encode: "))
            stored = encode(passcode)
            print("\nEncoder/Decoder Menu\n--------\n1. Encode\n2. Decode\n3. Quit")
            menu_option = int(input("\nPlease enter an option: "))

        if menu_option == 3:
            quit()
