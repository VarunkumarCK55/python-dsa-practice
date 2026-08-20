# Delete a node from a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third


# Value to delete
value = 20

current = first

# Search for the node
while current is not None:

    if current.next is not None and current.next.data == value:

        # Skip the node that needs to be deleted
        current.next = current.next.next
        break

    current = current.next


# Display linked list
current = first

print("Linked List after deletion:")

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")