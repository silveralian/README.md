print("WELCOME TO MY ADVENTURE!")

choice1 = input("You enter a house. Go upstairs or kitchen? ")

if choice1 == "kitchen":
    choice2 = input("You see a fridge and a cabinet. Choose fridge or cabinet: ")

    if choice2 == "fridge":
        choice3 = input("You find strange food. Eat it? yes or no: ")

        if choice3 == "yes":
            print("You ate the food and became sick. Ending 1.")
        else:
            print("You leave the food alone and escape safely. Ending 2.")

    else:
        choice3 = input("You find a mysterious box. Open it? yes or no: ")

        if choice3 == "yes":
            print("You find treasure! Ending 3.")
        else:
            print("You walk away and never know what was inside. Ending 4.")

else:
    choice2 = input("Upstairs you see a bedroom and bathroom. Choose bedroom or bathroom: ")

    if choice2 == "bedroom":
        choice3 = input("You see a closet. Open it? yes or no: ")

        if choice3 == "yes":
            print("A secret passage appears! Ending 5.")
        else:
            print("You go to sleep. Ending 6.")

    else:
        choice3 = input("You hear a noise behind the shower curtain. Check it? yes or no: ")

        if choice3 == "yes":
            print("You discover a hidden exit! Ending 7.")
        else:
            print("You run out of the house. Ending 8.")
