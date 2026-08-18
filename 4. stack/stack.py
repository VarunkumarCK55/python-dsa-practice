# Stack Practice Program
# Stack follows LIFO:
# Last In, First Out

stack = []

# -------------------------------------------------
# PUSH - Add an element to the top of the stack
# -------------------------------------------------

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)


# -------------------------------------------------
# PEEK - View the top element
# -------------------------------------------------

if len(stack) > 0:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")


# -------------------------------------------------
# POP - Remove the top element
# -------------------------------------------------

if len(stack) > 0:
    removed = stack.pop()
    print("Removed element:", removed)
else:
    print("Stack is empty")


print("Stack after pop:", stack)


# -------------------------------------------------
# PUSH another element
# -------------------------------------------------

stack.append(40)

print("Stack after adding 40:", stack)


# -------------------------------------------------
# Display all elements
# -------------------------------------------------

print("Current stack:")

for element in stack:
    print(element)