# Count how many times an element appears while searching

numbers = [10, 20, 10, 30, 10, 40]

search = 10
count = 0

for number in numbers:
    if number == search:
        count = count + 1

print("Array:", numbers)
print("Element:", search)
print("Occurrences:", count)