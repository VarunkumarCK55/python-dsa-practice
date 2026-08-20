# Create and display a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
first = Node(10)
second = Node(20)
third = Node(30)

# Connect nodes
first.next = second
second.next = third

# Start from the first node
current = first

print("Linked List:")

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
#output
#10 -> 20 -> 30 -> None