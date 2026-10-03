weight = float(input("Please enter your current earth weight: "))

print("I have information for the following planets:")
print("1. Venus")
print("2. Mars")
print("3. Jupiter")
print("4. Saturn")
print("5. Uranus")
print("6. Neptune")

planet = int(input("Which planet are you visiting? "))

if planet == 1:
    new_weight = weight * 0.78
elif planet == 2:
    new_weight = weight * 0.39
elif planet == 3:
    new_weight = weight * 2.65
elif planet == 4:
    new_weight = weight * 1.17
elif planet == 5:
    new_weight = weight * 1.05
elif planet == 6:
    new_weight = weight * 1.23
else:
    new_weight = weight

print(f"Your weight would be {new_weight}.")
