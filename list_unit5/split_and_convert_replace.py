
numbers_input = input("Enter numbers separated by spaces: ")

numbers = numbers_input.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(numbers)
