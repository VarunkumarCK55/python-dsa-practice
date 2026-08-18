# Search for an element using Binary Search
# Array must be sorted

numbers = [10, 20, 30, 40, 50, 60, 70]

search = 50

left = 0
right = len(numbers) - 1

found = False

while left <= right:

    middle = (left + right) // 2

    if numbers[middle] == search:
        found = True
        break

    elif search > numbers[middle]:
        left = middle + 1

    else:
        right = middle - 1

if found:
    print("Element found:", search)
else:
    print("Element not found:", search)