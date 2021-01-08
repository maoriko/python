"""
Create a progrem and check if the input is greater the number 10
if true
print: The number greater then 10
else: the number you entered is smaller then 10.
"""

num1 = 10
num2 = int(input("Please enter a number: "))

if num2 > num1:
    print("The number:", num2, "is greater then 10")
else:
    print("the number:", num2, "is smaller then 10")
