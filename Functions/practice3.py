import random

def min_max_amount(minVal, maxVal, amount):

    arr = []
    for i in range(amount):
        arr.append(random.randint(minVal, maxVal))

    return arr

print("Enter a 3 values to generate a random array")
user_min = int(input("Enter min: "))
user_max = int(input("Enter max: "))
user_amount = int(input("Enter amount: "))

arr = min_max_amount(user_min, user_max, user_amount)
print(arr)