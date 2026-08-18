# Search for an element using Linear Search

numbers = [10, 25, 30, 45, 50]

search = 30
found = False

for number in numbers:
    if number == search:
        found = True
        break

if found:
    print("Element found:", search)
else:
    print("Element not found:", search)