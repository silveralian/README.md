import random

while True:
    flip = random.randrange(1, 3)

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print(f"You flip a coin and it is... {coin}")

    again = input("Would you like to flip again (y/n)? ")

    if again != "y":
        break

# The program still works without again = "y" before the loop
# because while True always runs at least once.
# The value of again is created inside the loop before it is checked.
