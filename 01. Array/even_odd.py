# Find even and odd numbers in an array

numbers = [10, 15, 22, 31, 40, 55]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Array:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)