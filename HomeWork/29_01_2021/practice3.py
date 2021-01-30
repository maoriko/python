import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
low_case = s[0:25]
numbers = s[25:35]
capital = s[35:60]
special = s[60:]

def message():
    print("Hello, here is a password generator. ")
    print("Choose the length of your characters:")
    passGen()

def passGen():
    c = 0
    upper = int(input("How many capital letters you want?: "))
    spec = int(input("How many symbols you want?: "))
    num = int(input("How many numbers you want?: "))
    letters = int(input("How many letters you want?: "))
    c += upper + num + spec

    new_password = ""
    for i in range(upper):
        new_password += random.choice(capital)
    for x in range(spec):
        new_password += random.choice(special)
    for y in range(num):
        new_password += random.choice(numbers)
    for z in range(letters):
        new_password += random.choice(low_case)

    pass_word = list(new_password)
    new_pass = "".join(pass_word)
    print(new_pass)


message()