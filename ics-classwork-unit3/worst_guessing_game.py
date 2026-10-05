secret = 4

print("THE WORST NUMBER GUESSING GAME EVER!")

guess = int(input("I'm thinking of a number from 1-10. Guess it: "))

if guess == secret:
    print(f"You got it! The number was {secret}!")
else:
    print(f"Wrong! The secret number was {secret}.")
