class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def create_list(values):
    head = None
    temp = None 

    for value in values:
        new_node = Node(value)

        if head in None:
            head = new_node
            temp = new_node

        else:
            temp.next = new_node
            temp = new_node

    return head

def merge_lists(head1,head2): 
    dummy = Node(0)
    temp = dummy

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next

        temp = temp.next

        if head1 is not None:
            temp.next = head1

        else:
            temp.next = head2

    return dummy.next

def display(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print("None")

#input

list1 = list(map(int,input("Enter the first sorted list: ").split()))
list2 = list(map(int,input("Enter the second sorted list: ").split()))

head1 = create_list(list1)
head2 = create_list(list2)

print("First sorted list:")
display(head1)

print("Second sorted list:")
display(head2)

merged = merge_lists(head1, head2)

print("Merged sorted list:")
display(merged)
