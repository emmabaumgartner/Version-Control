# git add main.py
# git commit -m "added a commit"
# git push
# blue arrow = pull
# green check = commit
# green arrow up = push (move changes into GitHub)
'''
Lab 6: Version Control
Emma Baumgartner, Dalila Portal
Exercise in using GitHub through making a simple decode, encode program
Due 10/31/2023
'''
def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

def encode_password(password):
    # add 3 to each digit of the password
    password_encoded = []
    for digit in password:  # for char in len(0, len(password)
        if digit.isdigit():
            password_encoded.append(str(int(digit) + 3))
    return ''.join(password_encoded)

def decode_password(password):
    # take away 3 digits from the password?
    pass

while True:
    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        menu()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password_encoded = encode_password(password)
        if menu_option == 2:
            decoded_password = decode_password(password_encoded)
            print(f'The encoded password is {password_encoded} and the original password is {decoded_password}')
        if menu_option == 3:
            exit()


