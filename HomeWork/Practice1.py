"""
Date: 22/01/2021
Author: Maor Paz
"""
arr = [0, 1000]

while True:
    print(
        "Choose from menu:\n "
        "\n1)  Display min and max of values"
        "\n2)  Add values to the list"
        "\n3)  Sort list min to max"
        "\n4)  Sort list max to min"
        "\n5)  Average of the numbers"
        "\n6)  Index location of a number in the list "
        "\n7)  Find Duplicate numbers"
        "\n8)  Count Duplicate"
        "\n9)  Find missing number in the range 0-1000"
        "\n10) Clear all the list and insert 500 random numbers"
        "\n"
        "\nPress q to quit"
        "\n"
        "\nYour List:", arr)

    user_input = (input("\nWhat would you like to do now: "))



    if user_input == '1':
        print("")






















    if user_input == '2':
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
                if user_input != 'n':
                    continue
                else:
                    break
            else:
                break

    if user_input == '3':
        print()

    if user_input == '4':
        print()

    if user_input == '5':
        print()

    if user_input == '6':
        print()

    if user_input == '7':
        print()

    if user_input == '8':
        print()

    if user_input == '9':
        print()

    if user_input == '10':
        print()

    if user_input == "q":
        print("Bye!")
        break
# print(arr)
