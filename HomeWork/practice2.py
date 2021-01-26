"""
Practice 2
Date: 23/01/2021
Author: Maor Paz
"""


# Define the function of upper and lower
def num_str(num, string):
    if num == 1:
        return string.upper()
    elif num == 2:
        return string.lower()

    return string


while True:
    print(
        "\nTo make you string in CAPS press 1"
        "\nTo make you string in low case press 2"
    )
    try:
        user_input = int(input("Please choose 1 or 2: "))
        user_input_string = input("enter a string: ")
        if user_input == 1:
            print("\nThis is Your Upper Case String:", num_str(user_input, user_input_string))

            for i in user_input_string:
                print("\nThe ascii value of -", i.upper(), "is: ", ord(i))

        elif user_input == 2:
            print("\n This is Your Lower case String:", num_str(user_input, user_input_string))

            for i in user_input_string:
                print("\nThe ascii value of -", i.lower(), "is:", ord(i))

        elif user_input != 1 or user_input != 2 or user_input_string != str:
            print("\nThis is not allowed here Please choose 1 or 2 ")
            continue

    except (ValueError, TypeError):
        print("\nWrong value Please choose 1 or 2")
