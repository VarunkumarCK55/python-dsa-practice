# Reverse an array without using reverse()

numbers = [10, 20, 30, 40, 50]

reversed_array = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_array.append(numbers[i])

print("Original array:", numbers)
print("Reversed array:", reversed_array)