
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 50))

print("List:", end=" ")
for n in numbers:
    print(n, end=" ")

print()

target = int(input("Value to find: "))

for n in numbers:
    if n == target:
        print(target, "is in the list.")
