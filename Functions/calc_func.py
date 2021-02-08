# Simple calculator based on function


def my_sum(num1, num2):
    num3 = num1 + num2
    return num3


def my_sub(num1, num2):
    num3 = num1 - num2
    return num3


def my_multi(num1, num2):
    num3 = num1 * num2
    return num3


def my_div(num1, num2):
    num3 = num1 / num2
    return num3


user_input = -1
while user_input != 5:
    print("\nWhat would you like to do?: "
          "\n1) Addition"
          "\n2) Subtraction"
          "\n3) Multiplication"
          "\n4) Division"
          "\n5) Exit")

    user_input = int(input())
    if user_input == 5:
        print("Bye!")

    if user_input == 1:
        print("\nYou choose in Addition")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("\nThe result is: ", my_sum(num1, num2))

    if user_input == 2:
        print("\nYou choose Subtraction")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("\nThe result is: ", my_sub(num1, num2))

    if user_input == 3:
        print("\nYou choose Multiplication")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("\nThe result is: ", my_multi(num1, num2))

    if user_input == 4:
        print("\nYou choose Division")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("\nThe result is: ", my_div(num1, num2))