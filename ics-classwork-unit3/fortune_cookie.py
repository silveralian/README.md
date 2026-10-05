import random

fortune = random.randrange(1, 7)

if fortune == 1:
    message = "You will have a great day."
elif fortune == 2:
    message = "Something good is coming your way."
elif fortune == 3:
    message = "A new opportunity will appear soon."
elif fortune == 4:
    message = "Your hard work will pay off."
elif fortune == 5:
    message = "You will learn something important today."
else:
    message = "Good luck will find you soon."

print(f'Fortune cookie says: "{message}"')

print(
    random.randrange(1, 55),
    "-",
    random.randrange(1, 55),
    "-",
    random.randrange(1, 55),
    "-",
    random.randrange(1, 55),
    "-",
    random.randrange(1, 55),
    "-",
    random.randrange(1, 55)
)
