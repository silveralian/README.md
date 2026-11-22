
numbers_input = input("Enter numbers separated by spaces: ")

string_list = numbers_input.split()

numbers = []

for n in string_list:
    numbers.append(int(n))

print(numbers)
