class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node

    def addFirst(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def addLast(self, data):
        new_node = Node(data)

        current = self.head

        if self.head is None:
            self.head = new_node

        else:
            while current.next is not None:
                current = current.next

            current.next = new_node

    def deleteFirst(self):
        if self.head is None:
            return

        else:
            self.head = self.head.next

    def deleteLast(self):
        if self.head is None or self.head.next is None:
            self.head = None

        else:
            current = self.head

            while current.next.next is not None:
                current = current.next

            current.next = None

    def deleteAnyWhere(self,data):

        
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def main():
    linkedlist = LinkedList()

    linkedlist.append(10)
    linkedlist.append(20)
    linkedlist.append(30)
    linkedlist.addLast(69)
    linkedlist.append(40)
    linkedlist.addFirst(100)
    linkedlist.deleteFirst()
    linkedlist.deleteLast()
    linkedlist.deleteLast()

    linkedlist.display()


if __name__ == "__main__":
    main()
