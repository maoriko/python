def high_low(a, b):
    while True:
        if a > b:
            a -= 1
            print(a, end=",")
            break
        elif b > a:
            print("The upper limit is lower than the lower limit!")
            break

# high_low(10,7)
high_low(20,21)

