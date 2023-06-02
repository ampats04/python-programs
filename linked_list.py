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

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def main():
    linedlist = LinkedList()

    linedlist.append(10)
    linedlist.append(20)
    linedlist.append(30)

    linedlist.display()


if __name__ == "__main__":
    main()
