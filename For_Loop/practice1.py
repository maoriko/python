"""

"""

high_value = int(input("Please enter a value: \n"))
low_value = int(input("Please enter a second value: \n"))

print("The first value you choose is: ", high_value)
print("The second value you choose is: ", low_value)


for number in range(high_value, low_value):
    print("the range between the numbers", high_value, low_value, "is", number)
    pass

for number in range(low_value, high_value):
    print("the range between the numbers", low_value, high_value, "is", number)
    pass

if high_value > low_value:
    print("The higher value is:", high_value)
else:
    print("The higher value is:", low_value)