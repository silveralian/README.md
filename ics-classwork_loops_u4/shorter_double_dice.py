import random

print("HERE COME THE DICE!")
print()

while True:
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)

    print(f"Roll #1: {roll1}")
    print(f"Roll #2: {roll2}")
    print(f"The total is {roll1 + roll2}!")
    print()

    if roll1 == roll2:
        break
