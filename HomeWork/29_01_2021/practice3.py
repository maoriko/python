import random

def passGen():
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    letters = s[:26]
    numbers = s[26:36]
    capital = s[36:62]
    special = s[62:]
    final_password = ""
    password_string = ""
    try:
        print("Hello, here is a password generator. ")
        password_length = int(input("Please choose the length of you password: "))
    except ValueError:
        print(" only numbers are accepted here!")
        exit()

    user_letters = input("Add letters? y/n : ")
    user_numbers = input("Add numbers? y/n : ")
    user_capital = input("Add capital? y/n : ")
    user_special = input("Add symbols? y/n: ")

    if user_letters == 'y' or user_letters == 'Y':
        password_string += letters

    if user_numbers == 'y' or user_numbers == 'Y':
        password_string += numbers

    if user_capital == 'y' or user_capital == 'Y':
        password_string += capital

    if user_special == 'y' or user_special == 'Y':
        password_string += special

    for i in range(password_length):
        final_password += password_string[random.randint(0, len(password_string) - 1)]
    print(final_password)
    return final_password

passGen()
