# ---------------------- Student class ----------------------

class Student():
    def __init__(self, name, l_name, s_id, y_class, ):
        pass


class Node:
    def __init__(self, data=None, next=0):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, data):
         self.head = Node(data)

    def addNodeEnd(self, data):
        i = self.head

        while i.next:
            i = i.next

        i.next = Node(data)

    def addHead(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def countNodes(self):
        counter = 1
        i = self.head

        while i.next:
            counter += 1
            i = i.next

        return counter

    def printList(self):
        i = self.head

        while i:
            print(i)
            i = i.next

    def findInList(self, data):
        i = self.head

        while i:
            if i.data == data:
                return i
            i = i.next

        return None

    def removeNode(self, data):
        i = self.head

        # if we need to remove the first Node
        if i.data == data:
            self.head = self.head.next

        # find the object to remove and remove it: if found&deleted return 1 else 0
        while i:
            if i.next and i.next.data == data:
                i.next = i.next.next
                return 1

            i = i.next

        return 0

    def __str__(self):
        # initialize
        to_print = ""
        i = self.head

        # add data to to_print
        while i:
            to_print = to_print + str(i.data) + "\n"
            i = i.next

        # return string representing Linked List
        return to_print


ll = LinkedList(5)
ll.addNodeEnd(10)
ll.addNodeEnd(15)
ll.addHead(0)
ll.addNodeEnd(20)
ll.addNodeEnd(25)
ll.addHead(-5)
print(ll)


