# Find the position of an element using Linear Search

numbers = [10, 25, 30, 45, 50]

search = 45
position = -1

for i in range(len(numbers)):
    if numbers[i] == search:
        position = i
        break

if position != -1:
    print("Element:", search)
    print("Position:", position)
else:
    print("Element not found")