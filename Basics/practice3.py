num1 = int(input("Please enter a value: "))
num2 = int(input("please enter the second value: "))
num3 = num1+num2

if num3 > 0:
    print("The sum of numbers", num1, "+", num2, "=", num3, "is positive")
elif num3 == 0:
    print("The sum of numbers", num1, "+", num2, "=", num3, ",is natural")
else:
    print("The sum of numbers:", num1, "+", num2, "=", num3, "is negative")
