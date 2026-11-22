
import random

numbers = []

for i in range(1000):
    numbers.append(random.randint(10, 99))

for i in range(len(numbers)):
    print(numbers[i], end="  ")
