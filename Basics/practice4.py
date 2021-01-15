print("Welcome to a very scary roller coaster\n"
      "if you are smaller then 8 you are not welcome\n"
      "if you above 8 and your height is above 115CM\n"
      "Then get in")

age = int(input("Please enter your age: "))
height = int(input("Please enter your height :"))

if age < 8 or age < 18 or height < 115:
    print("Your age is", age, "your height is", height, "You are to small for this")
if age > 120 or height > 220:
    print("You must be kidding on me\n"
          "The amount of years must be lower then 120\n"
          "The height must be lower then 220")
else:
    print("hup in")
