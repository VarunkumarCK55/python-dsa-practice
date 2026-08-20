# Insert a new node at the beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
first = Node(20)
second = Node(30)

first.next = second


# Create a new node
new_node = Node(10)

# Connect new node to the old first node
new_node.next = first

# Make new node the first node
first = new_node


# Display linked list
current = first

print("Linked List:")

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")