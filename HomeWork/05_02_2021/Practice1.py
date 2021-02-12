class My_Stack:

    def __init__(self, arr=[], size=5):
        self.__arr = arr
        self.__size = size

    def push(self, num_to_push):
        if len(self.__arr) < self.__size:
            self.__arr.append(num_to_push)

    def pop(self):
        if not self.is_empty():
            return self.__arr.pop()

    def is_empty(self):
        if len(self.__arr) == 0:
            return True
        return False

    def print(self):
        print("Stack size:", self.__size, ", Elements:")
        for i in self.__arr:
            print(i)

    def set_size(self, new_size):
        self.__size = new_size

    def top(self):
        return self.__arr[-1]

    def __add__(self, other):
        return My_Stack(self.__arr.copy() + other.__arr.copy(), self.__size + other.__size + 10)

    def __str__(self):
        return "Size: " + str(self.__size) + " Stack: " + str(self.__arr)


def func(check_str):

    close_p = ["(", "[", "{"]
    open_p = [")", "]", "}"]

    s = My_Stack()

    for i in check_str:

        if i in open_p:
            s.push(i)
            continue

        if i in close_p:
            temp = s.pop

            if temp == None:
                return False

            if close_p.index(i) != open_p.index(temp):
                return False
            else:
                continue

    if s.is_empty() == True:
        return True
    else:
        return False