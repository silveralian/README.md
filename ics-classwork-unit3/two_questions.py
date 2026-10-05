print("TWO QUESTIONS!")
print("Think of an object, and I'll try to guess it.")

category = input("Is it animal, vegetable, or mineral? ")
big = input("Is it bigger than a breadbox? ")

if category == "animal":
    if big == "yes":
        print("My guess is a moose.")
    else:
        print("My guess is a squirrel.")

elif category == "vegetable":
    if big == "yes":
        print("My guess is a watermelon.")
    else:
        print("My guess is a carrot.")

elif category == "mineral":
    if big == "yes":
        print("My guess is a Camaro.")
    else:
        print("My guess is a paper clip.")
