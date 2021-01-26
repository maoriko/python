"""
Practice 1
Date: 22/01/2021
Author: Maor Paz
"""
import random

arr = []


# Define the Maximum function
def maximum_func(nums):
    my_max = 0
    for i in nums:
        if i > my_max:
            my_max = i
    return my_max


# Define the Minimum function
def minimum_func(nums):
    my_min = 0
    for i in nums:
        if i < my_min:
            my_min = i
    return my_min


def unique(l, num):
    if num not in l:
        l.append(num)

    return l


while True:
    print(
        "\nChoose from menu:\n "
        "\n1)  Add values to the list"
        "\n2)  Remove from list"
        "\n3)  Display min Value "
        "\n4)  Display max values"
        "\n5)  Average of the numbers"
        "\n6)  Print all numbers within the list"
        "\n7)  Sort list min to max"
        "\n8)  Sort list max to min"
        "\n9)  Clear all the list and insert 500 random numbers"
        "\n"
        "\nPress q to quit"
        "\n"
        "\nYour List:", arr)

    user_input = (input("\nWhat would you like to do now: "))

    if user_input == "q":
        print("Bye!")
        break

    # Add multiple numbers or 1
    if user_input == '1':

        while True:
            try:
                user_input = int(input("\nAdd in range 1-1000 to list: "))
                if user_input not in range(0,1000):
                    print("You tried to add,", user_input, "Which is not allowed here, Going to main menu ")
                    break
            except ValueError:
                print("This is not allowed here!")
                break

            print("You choose to insert", user_input, "to your list:", arr)
            ask = input("\nAre you sure you want to insert this number? y/n: ")
            if ask == 'y':
                arr.append(user_input)
                print("\nA number", user_input, "added to your list:", arr)

            user_input = input("\nWould you like to add another? y/n ")
            if user_input == 'y':
                continue
            elif user_input == 'n':
                break
            elif ask != 'y' or ask != 'n':
                print("\nI don't know what to do, going to main menu!")
                break
            else:
                print("\nNot Allowed going to top")
                break

        print("\nReturning to main menu")
        continue

    # Remove from list.
    if user_input == '2':
        print("This is your list:", arr)
        user_input = int(input("What number would you like to remove: "))

        while True:
            if user_input in arr:
                print("the number", user_input, "successfully Removed")
                arr.remove(user_input)
                print(arr)
                break

            elif user_input not in arr:
                print("\n The number: ", user_input, "does not exist!, Try again")
                break
            continue

    # Display min Value
    if user_input == '3':
        print("\nThe minimum number is:\n", minimum_func(arr))

    # Display max Value
    if user_input == '4':
        print("The maximum value in the list is:\n", maximum_func(arr))

    # Average of the numbers
    if user_input == '5':
        i = len(arr)
        while i < maximum_func(arr):
            print("\nThe average numbe is:", maximum_func(arr) / i)
            break

    # Print all numbers within the list
    if user_input == '6':
        i = 1
        while i < maximum_func(arr) and i not in arr:
            print(i)
            i += 1

    # Sort list min to max
    if user_input == '7':
        print("\nYou choose to sort you list from min to max\n")
        arr.sort()
        print("\nHere is your sotred list min to max", arr)

    # Sort from max to min
    if user_input == '8':
        print("\nYou choose to sort you list from max to min")
        arr.sort(reverse=True)
        print("\nHere is your sotred list from max to min")

    # Clear all the list and insert 500 random numbers
    # if user_input == '9':
    if user_input == '9':
        print("Your list is cleared!")
        arr = []
        for i in range(0, 500):
            n = random.randint(0, 500)
            arr.append(n)
            print(arr, end="")
        continue
