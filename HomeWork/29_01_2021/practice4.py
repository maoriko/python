def score_total(password):
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    low_case = s[0:26]
    s_low = 0
    numbers = s[26:36]
    s_nums = 0
    capital = s[36:62]
    s_cap = 0
    special = s[62:]
    s_special = 0
    len_points = 0
    len_letters = len(password)
    bonus_point = 0

    while True:
        if len_letters < 6:
            len_points += 1
            break
        elif len_letters == 6 or len_letters == 7 or len_letters == 8:
            len_points += 2
            break
        elif len_letters > 8:
            len_points += 3
            break

    for i in passwd:
        if i in low_case:
            s_low += 1
            break
    for i in passwd:
        if i in numbers:
            s_nums += 1
            break
    for i in passwd:
        if i in capital:
            s_cap += 1
            break
    for i in passwd:
        if i in special:
            s_special += 2
            break

    if password in special and password in capital or low_case or numbers:
        bonus_point += 1
    elif password in special and password in capital and password in special or numbers:
        bonus_point += 2

    total = s_low + s_nums + s_cap + s_special + len_points + bonus_point

    if total <= 4:
        print("Your password is weak.")
    elif total == 5 or total == 6:
        print("Your password is medium")
    elif total == 7:
        print("Your password strong")
    elif total > 8:
        print("You password is very strong")
    return total


while True:
    print("In front of you a password checker, Here is the score table:\n"
          "4 points = Weak password\n"
          "5-6 points = Medium password\n"
          "7 points = Strong password\n"
          "8 points and above = Very strong password\n ")
    passwd = input("To check you password score type it here: ")
    print("Total Score is: ", score_total(passwd))

    try:
        start_again = input("would you like to check another password? y/n: ")
        if start_again == 'y' or start_again == 'Y':
            continue
        elif start_again == 'n' or start_again == 'N':
            print('Bye!')
            break
    except ValueError:
        print("Unknown command")
        continue