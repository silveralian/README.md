import random

secret = random.randrange(1, 101)

print("I'm thinking of a number between 1-100. Try to guess it.")
guess = int(input("> "))

if guess == secret:
    print("You guessed it! What are the odds?!?")
elif guess > secret:
    print(f"Sorry, you are too high. I was thinking of {secret}.")
else:
    print(f"Sorry, you are too low. I was thinking of {secret}.")
