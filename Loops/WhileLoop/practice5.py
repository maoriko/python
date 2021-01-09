"""
Write a program whom get input from user and check if this is a even number or odd, the range between 100 to 350
"""

number = int(input("Please choose a number between 100 - 350: "))

while number <= 350 or number >= 100:
    # print("you picked even number: ", number)
    if number % 2 == 0:
        print("This is even number", number)
        break
    elif number >= 350 or number <= 100:
        print("You are out of range the number", number, "will not be excepted")
        break
    else:
        print("This is odd number", number)
    number = number + 2