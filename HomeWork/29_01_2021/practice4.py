s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
low_case = s[0:26]
numbers = s[26:36]
capital = s[36:62]
special = s[62:]
score = 0


password = input('Enter your password > ')


def find_password_strength(password):
    password_length = len(password)
    password_length_score = 0
    password_strength = 0
    lowercase_count = 0
    uppercase_count = 0
    numbers_count = 0
    special_count = 0
    bonus_count = 0
    weak_password = 4
    medium_password = 6
    strong_password = 7
    very_strong_password = 8

    if password_length < 6:
        password_length_score +=1
    while password_length in range(6, 8):
        password_length_score += 2
        break
    else:
        password_length_score += 3


    for char in password:
        password_strength += 1
        if char in low_case:
            lowercase_count += 1
        if char in capital:
            uppercase_count += 1
        if char in numbers:
            numbers_count += 1
        if char in special:
            special_count += 2
        if char in special and char in low_case or char in numbers or char in capital:
            bonus_count += 2

    character_sum = (lowercase_count + uppercase_count + numbers_count + special_count + bonus_count + password_length_score)
    print(character_sum)

    password_strength += character_sum
    print('Your passwords score was {}', password_strength)

    if weak_password <= password_strength < strong_password:
        print('Password strength is weak.')

    elif password_strength < medium_password:
        print('Password strength is medium.')

    elif password_strength >= strong_password:
        print('Password strength is Strong.')

    elif password_strength >= very_strong_password:
        print("Password strength is very strong")


find_password_strength(password)





































# password_input = input("Here is a password checker:\n To start, enter your password: ")
# password_list = list(password_input)
#
#
# def len_check():
#
#     i = len(password_input)
#     return i
#
#
# def check_letters():
#     if password_input in str(low_case):
#         return
#
#
# def check_numbers():
#     if password_input in str(numbers):
#         return
#
#
# def check_capital():
#     if password_input in str(capital):
#         return
#
#
# def check_special():
#     if password_input in str(special):
#         return
#
#
# while True:
#     for i in range(6, 8):
#         if i <= 6:
#             score += 1
#             print("Password too short your score is", score)
#             pass
#         elif 6 >= i < 8:
#             print("the len is good you get", score + 2)
#             continue
#         elif i > 8:
#             print("The len is very good! you got", score + 3)
#             score += 3
#
#     break
