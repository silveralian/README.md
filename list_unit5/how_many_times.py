
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 50))

print("List:", end=" ")
for n in numbers:
    print(n, end=" ")

print()

target = int(input("Value to find: "))
count = 0

for n in numbers:
    if n == target:
        count += 1

print(target, "was found", count, "times.")
