import random

print("Welcome to the guess game! \nPlease Enter 2 numbers ")
minVal = (int(input("Enter the low range: ")))
maxVal = (int(input("Enter thr max range: ")))

n = random.randint(minVal, maxVal)
print(n)

count = 0
guess_user_input = -1

while guess_user_input != n and count < 5:
    guess_user_input = (int(input("Guess your number: ")))

    if guess_user_input == n:
        print("Great!\n you guessed after", count + 1, "times")
        break

    elif guess_user_input < n:
        print("Try bigger number")

    elif guess_user_input > n:
        print("Try a smaller number")
    else:
        print("try again")
    count += 1