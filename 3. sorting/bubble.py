# Sort an array using Bubble Sort

numbers = [50, 20, 40, 10, 30]

print("Before sorting:", numbers)

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("After sorting:", numbers)