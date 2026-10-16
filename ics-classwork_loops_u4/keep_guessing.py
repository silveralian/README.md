import random

secret = random.randrange(1, 11)

print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your guess: "))

while guess != secret:
    print("That is incorrect. Guess again.")
    guess = int(input("Your guess: "))

print("That's right! You're a good guesser.")

dice_doubles.py 
import random

print("HERE COMES THE DICE!")
print()

roll1 = random.randrange(1, 7)
roll2 = random.randrange(1, 7)

while roll1 != roll2:
    print(f"Roll #1: {roll1}")
    print(f"Roll #2: {roll2}")
    print(f"The total is {roll1 + roll2}!")
    print()

    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)

print(f"Roll #1: {roll1}")
print(f"Roll #2: {roll2}")
print(f"The total is {roll1 + roll2}!")
