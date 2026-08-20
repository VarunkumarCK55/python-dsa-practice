# Find the middle element of a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth


# Slow and fast pointers
slow = first
fast = first

while fast is not None and fast.next is not None:

    slow = slow.next
    fast = fast.next.next


print("Middle element:", slow.data)