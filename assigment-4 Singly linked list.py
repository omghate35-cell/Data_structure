class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Create / Insert at End
    def create(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete Node
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Element not found")
            return

        prev.next = temp.next

    # Search
    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                print("Element found at position", pos)
                return
            temp = temp.next
            pos += 1

        print("Element not found")

    # Reverse List
    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    # Insert in Sorted Order
    def sorted_insert(self, data):
        new_node = Node(data)

        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next and temp.next.data < data:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


# Driver Program
sll = SinglyLinkedList()

while True:
    print("\n1.Create")
    print("2.Display")
    print("3.Insert at Beginning")
    print("4.Delete")
    print("5.Search")
    print("6.Reverse")
    print("7.Sorted Insert")
    print("8.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        n = int(input("Enter element: "))
        sll.create(n)

    elif choice == 2:
        sll.display()

    elif choice == 3:
        n = int(input("Enter element: "))
        sll.insert_begin(n)

    elif choice == 4:
        n = int(input("Enter element to delete: "))
        sll.delete(n)

    elif choice == 5:
        n = int(input("Enter element to search: "))
        sll.search(n)

    elif choice == 6:
        sll.reverse()
        print("List Reversed")

    elif choice == 7:
        n = int(input("Enter element: "))
        sll.sorted_insert(n)

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")