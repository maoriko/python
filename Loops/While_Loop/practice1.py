
n = int(input("Please enter a number:"))

while n < 1000:
    if n % 2 == 0:
        print(" This is a even number", n)
    else:
        print("This is a odd number", n)
    n = n + 2
