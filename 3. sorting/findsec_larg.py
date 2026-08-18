# Find the second largest element after understanding sorting

numbers = [10, 50, 30, 40, 20]

# First sort the array
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

second_largest = numbers[-2]

print("Sorted array:", numbers)
print("Second largest:", second_largest)