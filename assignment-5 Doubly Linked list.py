class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Create / Insert at End
    def create(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev

            last.next = new_node
            new_node.prev = last

            new_node.next = self.head
            self.head.prev = new_node

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Head)")

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev

            new_node.next = self.head
            new_node.prev = last

            last.next = new_node
            self.head.prev = new_node

            self.head = new_node

    # Delete Node
    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == key:
                break
            temp = temp.next
            if temp == self.head:
                print("Element not found")
                return

        if temp.next == temp:
            self.head = None

        elif temp == self.head:
            last = self.head.prev
            self.head = self.head.next
            last.next = self.head
            self.head.prev = last

        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        print("Deleted Successfully")

    # Search
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        pos = 1

        while True:
            if temp.data == key:
                print("Element found at position", pos)
                return

            temp = temp.next
            pos += 1

            if temp == self.head:
                break

        print("Element not found")


# Driver Program
dll = DoublyCircularLinkedList()

while True:
    print("\n1.Create")
    print("2.Display")
    print("3.Insert at Beginning")
    print("4.Delete")
    print("5.Search")
    print("6.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        dll.create(x)

    elif choice == 2:
        dll.display()

    elif choice == 3:
        x = int(input("Enter element: "))
        dll.insert_begin(x)

    elif choice == 4:
        x = int(input("Enter element to delete: "))
        dll.delete(x)

    elif choice == 5:
        x = int(input("Enter element to search: "))
        dll.search(x)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")