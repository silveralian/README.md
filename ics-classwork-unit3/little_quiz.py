score = 0

print("Welcome to my quiz!")

answer = input("1. Is Python a programming language? ")

if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What is 7 % 2? ")

if answer == "1":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. Does input() return a string by default? ")

if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"You got {score} out of 3.")
