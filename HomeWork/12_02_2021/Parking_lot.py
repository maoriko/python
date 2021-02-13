from os import times
import time

user_name = input("To start create user name:")
user_password = input("Create Password: ")


def user_check(user):
    if user == user_name:
        return True
    else:
        print("Wrong username!")
        return None


def user_pass(passwd):
    if passwd == user_password:
        return True
    else:
        print("Wrong password!")
        return None


class Car:
    def __init__(self, car_num=[]):
        self.__car_num = car_num

    def add_car(self, car_num_add):
        for car_num_add in self.__car_num:
            if car_num_add not in self.__car_num and car_num_add == 7:
                self.__car_num.append(car_num_add)
                return car_num_add
            
            elif car_num_add in self.__car_num:
                print("The car number", car_num_add, "already exist!")
                return car_num_add

            elif car_num_add > 6:
                print("You have too much numbers in the car section", car_num_add)
                return car_num_add

            elif car_num_add < 8:
                print("you have less numbers in the car section", car_num_add)
                return car_num_add

            break

        return car_num_add

    def add_phone(self, phone_num_add):
        if phone_num_add not in self.__car_num and phone_num_add == 10:
            self.__car_num.append(phone_num_add)
            return phone_num_add

        elif phone_num_add in self.__car_num:
            print("The phone number", phone_num_add, "already exist!")
            return phone_num_add

        elif phone_num_add > 10:
            print("You have too much numbers in the phone section")
            return phone_num_add

        elif phone_num_add < 10:
            print("you have less numbers in the phone section")
            return phone_num_add

        return phone_num_add

    def car_type(self):
        pass

    def time_arrive(self):
        pass

    def print_car(self):
        for i in self.__car_num:
            if len(i) == 7:
                print("car", i)
            if len(i) == 10:
                print("phone:", i)


class Parking_lot:

    def __init__(self):
        pass


while True:
    print("\nWelcome, Here you can manage your parking lot\n"
          "Please make your choice :\n"
          "1) Initialize new parking (user name and password required)\n"
          "2) Add new vehicle \n"
          "3) Remove vehicle \n"
          "4) Change price per hour (user name and password required)\n"
          "5) Change vehicle capacity (user name and password required)\n"
          "6) print all vehicles above 24 hour\n"
          "7) print all vehicles in the parking lot\n"
          "8) exit")

    user_menu = int(input(""))

    if user_menu == 1:
        temp_user = input("Please type your username: ")
        temp_passwd = input("Please type your password: ")

        if user_check(temp_user) and user_pass(temp_passwd):
            try:
                enter_car = int(input("Add car number by 7 numbers long "))
                # enter_phone = int(input("Add phone number by 10 numbers long "))
                c = Car()
                c.add_car(enter_car)
                # c.add_phone(enter_phone)
                c.print_car()

            except ValueError:
                print("Only numbers allowed here")
                break

    elif user_menu == 2:
        pass

    elif user_menu == 3:
        pass

    elif user_menu == 4:
        pass

    elif user_menu == 5:
        pass

    elif user_menu == 6:
        pass

    elif user_menu == 7:
        pass

    elif user_menu == 8:
        exit("Bye!")

# self.car_num.append(phone_num_add)
# return phone_num_add
