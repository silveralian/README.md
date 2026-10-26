import random

secret = random.randrange(1, 11)
tries = 0

print("I have chosen a number between 1 and 10. Try to guess it.")

while True:
    guess = int(input("Your guess: "))
    tries += 1

    if guess == secret:
        break

    print("That is incorrect. Guess again.")

print("That's right! You're a good guesser.")
print(f"It only took you {tries} tries.")
