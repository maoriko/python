import random

print("Welcome to the Guess game! \nPlease Enter 2 numbers and guess what is the number!")
minVal = (int(input("Enter the low range: ")))
maxVal = (int(input("Enter the max range: ")))

rand_num = random.randint(minVal, maxVal)
print(rand_num)

count = 5
guess_user_input = -1

while guess_user_input != rand_num and count > 0:
    guess_user_input = (int(input("Guess your number: ")))

    if guess_user_input == rand_num:
        print("Great!\nYou guessed after", count - 1, "times")
        break

    elif guess_user_input < rand_num:
        print("Try bigger number\nYou have", count - 1, "times left")

    elif guess_user_input > rand_num:
        print("Try smaller number\nYou have", count - 1, "times left")
    count -= 1

else:
    print("Better luck next time! ")
