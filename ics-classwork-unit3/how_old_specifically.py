name = input("Hey, what's your name? ")
age = int(input(f"Ok, {name}, how old are you? "))

if age < 16:
    print(f"You can't drive, {name}.")
elif age < 18:
    print(f"You can drive but you can't vote, {name}.")
elif age < 21:
    print(f"You can vote but you can't rent a car, {name}.")
else:
    print(f"You can do pretty much anything, {name}.")
