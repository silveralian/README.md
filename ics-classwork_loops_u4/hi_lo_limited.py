import random

secret = random.randrange(1, 101)
tries = 1

print("I'm thinking of a number between 1-100. You have 7 guesses.")

guess = int(input("First guess: "))

while guess != secret and tries < 7:

    if guess > secret:
        print("Sorry, that guess is too high.")

    else:
        print("Sorry, you are too low.")

    tries += 1
    guess = int(input(f"Guess # {tries}: "))

if guess == secret:
    print("You guessed it! What are the odds?!?")

else:
    print("Sorry, you didn't guess it in 7 tries. You lose.")
