# Sort an array using Insertion Sort

numbers = [40, 20, 50, 10, 30]

print("Before sorting:", numbers)

for i in range(1, len(numbers)):

    current = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = current

print("After sorting:", numbers)