# Queue Practice Program
# Queue follows FIFO:
# First In, First Out

from collections import deque

queue = deque()

# -------------------------------------------------
# ENQUEUE - Add an element to the queue
# -------------------------------------------------

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", list(queue))


# -------------------------------------------------
# FRONT - View the first element
# -------------------------------------------------

if len(queue) > 0:
    print("Front element:", queue[0])
else:
    print("Queue is empty")


# -------------------------------------------------
# DEQUEUE - Remove the first element
# -------------------------------------------------

if len(queue) > 0:
    removed = queue.popleft()
    print("Removed element:", removed)
else:
    print("Queue is empty")


print("Queue after dequeue:", list(queue))


# -------------------------------------------------
# ENQUEUE another element
# -------------------------------------------------

queue.append(40)

print("Queue after adding 40:", list(queue))


# -------------------------------------------------
# Display all elements
# -------------------------------------------------

print("Current queue:")

for element in queue:
    print(element)