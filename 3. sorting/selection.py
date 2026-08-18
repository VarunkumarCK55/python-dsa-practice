# Sort an array using Selection Sort

numbers = [40, 10, 50, 20, 30]

print("Before sorting:", numbers)

for i in range(len(numbers)):

    smallest = i

    for j in range(i + 1, len(numbers)):

        if numbers[j] < numbers[smallest]:
            smallest = j

    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

print("After sorting:", numbers)