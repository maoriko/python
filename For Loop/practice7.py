"""
Write a program to print numbers in range between 500-1000
"""

for i in range(500, 1001):
    print(i)


"""
Create array with numbers of your choice,
write a program to print the sum of the array
"""

my_arr = [1, 7, 9, 34, 64, 76, 54, 675, 73, 5]
i = sum(my_arr)
print(i)

"""
Write a program containing this string:
my_str = "Hello my name is Maor and i love programming in python" 
and slice :

Hello I programming in python

Maor love python

gnimmaragorP evol roaM  
"""

my_str2 = "Hello my name is Maor and i love programming in python"

# Check the length:
print(len(my_str2))

# Use Find:
print(my_str2.find("programming"))

# Hello I programming in python
print(my_str2[0:6] + my_str2[26:27] + my_str2[32:])

# Maor love python
print(my_str2[17:21] + my_str2[27:32] + my_str2[47:])

# Print in reverse: gnimmaragorP evol roaM
print(my_str2[43:32:-1] + my_str2[32:27:-1] + my_str2[21:16:-1])


