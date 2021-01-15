def high_low():
    return "another day"

user_input=int(input("Please write a numer 0 or 1: "))

if user_input == 1:
    print(high_low().upper())
elif user_input == 0:
    print(high_low().lower())
else:
    print("Wrong!")