
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

for i in range(len(numbers)):
    print("Slot", i, "contains a", numbers[i])
