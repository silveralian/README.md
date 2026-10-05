import random

secret = random.randrange(1, 11)

print("I'm thinking of a number from 1 to 10.")
guess = int(input("Your guess: "))

if guess == secret:
    print(f"That's right! My secret number was {secret}!")
else:
    print(f"Sorry, but I was really thinking of {secret}.")
