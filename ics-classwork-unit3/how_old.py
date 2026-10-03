name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 16:
    print(f"{name}, you cannot drive.")

if age < 18:
    print(f"{name}, you cannot vote.")

if age < 21:
    print(f"{name}, you cannot rent a car.")

if age >= 21:
    print(f"{name}, you can do anything that's legal.")
