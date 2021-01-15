user_input = -1
while user_input != 0:
    print("Welcome, Please make you choice: \n0) Exit\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
    user_input = int(input())
    if user_input == 0:
        print("Bye!")

    if user_input == 1:
        print("you choose in Addition")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = num1 + num2
        print("the result of", num1, "+", num2, "is", num3)

    if user_input == 2:
        print("you choose Subtraction")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = num1 - num2
        print("the result of", num1, "-", num2, "is", num3)

    if user_input == 3:
        print("you choose Multiplication")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = num1 * num2
        print("the result of", num1, "*", num2, "is", num3)

    if user_input == 4:
        print("you choose Division")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(num1 / num2)
        print("the result of", num1, "/", num2, "is", num3)
