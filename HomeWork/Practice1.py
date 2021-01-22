"""
Date: 22/01/2021
Author: Maor Paz
"""
import random

arr = [0, 100, 1000]

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
        sure = -1
        another = -1
        while sure != 'n' or another != 'n':
            add_num = int(input("\nAdd number to list: "))
            print("You choose to insert", add_num, "to your list:", arr)
            sure = input("\nAre you sure you want to insert this number? y/n: ")

            if sure == 'y':
                num_to_add = arr.append(add_num)
                print("\nA number", add_num, "added to your list:", arr, "\n You like to add another?")

                user_input = input("Enter y/n: ")
                while user_input != 'y':

                    if user_input == 'n':
                        print("\nGoing to the main menu")
                        break

                    elif user_input != 'y' or user_input != 'n':
                        print("\nNot Allowed! type y / n")

                    else:
                        break
                continue
            continue
        else:
            break

# Remove from list.
    if user_input == '2':
        print("This is your list:", arr)
        user_input = int(input("What number would you like to remove: "))
        # print(arr)
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
        for i in arr:
            i += 1
            count = sum(arr)
            print("The average is", count / i)

# Print all numbers within the list
    if user_input == '6':
        i = 1
        while maximum_func(arr) > i > minimum_func(arr):
            print(i)
            i += 1

# Sort list min to max
    if user_input == '7':
        print("\nYou choose to sort you list from min to max\n")
        print("Here is your sotred list", sorted(arr))

# Sort from max to min
    if user_input == '8':
        print("\nYou choose to sort you list from max to min\n\n")
        print(sorted(arr, reverse=True))

# Clear all the list and insert 500 random numbers
    if user_input == '9':
        print("Your list is cleared!")
        arr = [random.randint(0, 500)]
        i = 1
        while i < 500:
            print(i)
            i += 1