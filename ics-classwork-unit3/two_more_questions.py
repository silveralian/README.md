print("TWO MORE QUESTIONS!")

place = input("Does it belong inside, outside, or both? ")
alive = input("Is it alive? yes or no: ")

if place == "inside" and alive == "yes":
    print("You are thinking of a houseplant.")

if place == "inside" and alive == "no":
    print("You are thinking of a shower curtain.")

if place == "outside" and alive == "yes":
    print("You are thinking of a bison.")

if place == "outside" and alive == "no":
    print("You are thinking of a billboard.")

if place == "both" and alive == "yes":
    print("You are thinking of a dog.")

if place == "both" and alive == "no":
    print("You are thinking of a cell phone.")
