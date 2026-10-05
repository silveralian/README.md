import random

ace = random.randrange(1, 4)

print("You slide up to Fast Eddie's card table and plop down your cash.")
print("He glances at you out of the corner of his eye and starts shuffling.")
print()
print("He lays down three cards.")
print()
print("Which one is the ace?")
print()
print("##  ##  ##")
print("##  ##  ##")
print("1   2   3")

guess = int(input("> "))

print()

if guess == ace:
    print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
else:
    print(f"Ha! Fast Eddie wins again! The ace was card number {ace}.")

if ace == 1:
    print("AA  ##  ##")
    print("AA  ##  ##")
elif ace == 2:
    print("##  AA  ##")
    print("##  AA  ##")
else:
    print("##  ##  AA")
    print("##  ##  AA")

print("1   2   3")
