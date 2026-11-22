
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 50))

print("List:", end=" ")
for n in numbers:
    print(n, end=" ")

print()

target = int(input("Value to find: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(target, "is at index", str(i) + ".")
        found = True

if found == False:
    print(target, "is not in the list.")
