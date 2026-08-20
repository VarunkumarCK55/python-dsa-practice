# Reverse a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

first.next = second
second.next = third
third.next = fourth


# Reverse the linked list
previous = None
current = first

while current is not None:

    next_node = current.next

    current.next = previous

    previous = current
    current = next_node


# Previous becomes the new first node
first = previous


# Display reversed list
current = first

print("Reversed Linked List:")

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")