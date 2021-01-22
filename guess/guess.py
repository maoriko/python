import random


print("Welcome to the Guessing number!\n Rules:\n  Insert 2 number for your choice\n Then guess the random number between theme!")
print("  You have 5 tries so choose wisely!")
minVal = (int(input("Enter the low number for you choice: ")))
maxVal = (int(input("Enter the high number for you choice: ")))

rand_num = random.randint(minVal, maxVal)
# print(rand_num)

count = 5
guess_user_input = -1

while guess_user_input != rand_num and count > 0:
    guess_user_input = (int(input("Guess your number: ")))

    if count == 0:
        break

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


