from datetime import datetime, timedelta


# --------------------------
# Global Functions
# --------------------------


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_dict = {'username': username, 'password': password}

    return user_dict


def login(user_dict):
    username = input("Enter username: ")
    if username == user_dict['username']:
        password = input("Enter password: ")
        if password == user_dict['password']:
            return True

    return False


class ParkingLot:
    def __init__(self):
        self.lot = []
        self.__price_ph = 15
        self.__capacity = 10

    def insert_car(self, new_car):
        if len(self.lot) < self.__capacity:
            self.lot.append(new_car)
            return True
        if len(self.lot) >= 0.8 * self.__capacity:
            print("parking lot is over 80% full")
        else:
            print("lot is full")
            return False

    def remove_car(self, plate_to_remove):
        for elem in self.lot:
            if elem.get_plate() == plate_to_remove:
                self.lot.remove(elem)
                return True
        return False

    def get_price(self):
        return self.__price_ph

    def set_price(self, new_price):
        self.__price_ph = new_price
        return self.__price_ph

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, new_space):
        self.__capacity = new_space
        return self.__capacity

    def print_lot(self):
        for elem in self.lot:
            print(elem)
            print()

    def report_over_24(self):
        over_24 = []
        for elem in self.lot:
            entry_time = elem.get_entry_time()
            exit_time = datetime.now()
            time_diff = exit_time - entry_time
            if (time_diff.seconds // 3600) >= 24:
                over_24.append(elem)

        for i in over_24:
            print(i)


class Car:

    def __init__(self, plate, car_type, phone):
        self.plate = plate
        self.car_type = car_type
        self.phone = phone
        self.entry_time = datetime.now()

    def set_new_phone(self, new_phone):
        self.phone = new_phone

    def get_plate(self):
        return self.plate

    def get_entry_time(self):
        return self.entry_time

    def __str__(self):
        return f"Plate: {self.plate}\nModel: {self.car_type}\nPhone: {self.phone}"


def menu():
    menu_dict = {
        '1': "New Parking (Admin)",
        '2': "Add Vehicle",
        '3': "Remove Vehicle",
        '4': "Change hourly price (Admin)",
        '5': "Change lot capacity (Admin)",
        '6': "Above 24 hours report",
        '7': "Print all vehicles",
        '8': "Quit"
    }
    for key, val in menu_dict.items():
        print(f"{key}) {val}")

    return input('>>> ')


def get_car():
    while True:
        car_plate = input("Enter plate number: ")
        car_type = input("Enter type: ")
        car_phone = input("Enter phone number: ")
        try:
            car = Car(plate=car_plate, car_type=car_type, phone=car_phone)
            return car
        except Exception as e:
            print("Oops, there is an error in one or more of the inputs")
            print("Error:", e)
            continue


if __name__ == '__main__':
    parking = ParkingLot()  # creating initial parking lot
    users = register()

    while True:
        choice = menu()

        if choice == '1':
            if login(users):
                parking = ParkingLot()  # creating new parking lot
            else:
                print("Invalid username or password\n")

        elif choice == '2':
            car = get_car()
            print(car.get_entry_time())
            parking.insert_car(car)

        elif choice == '3':
            plate_to_remove = input("Enter plate to remove: ")
            parking.remove_car(plate_to_remove)

        elif choice == '4':
            if login(users):
                user_price = input("What is the new price? ")
                parking.set_price(user_price)

        elif choice == '5':
            if login(users):
                user_lot = input("What is the new price? ")
                parking.set_capacity(user_lot)

        elif choice == '6':
            parking.report_over_24()

        elif choice == '7':
            parking.print_lot()

        elif choice == '8':
            exit("Bye!")