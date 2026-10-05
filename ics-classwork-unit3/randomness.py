import random

random.seed(123)

x = random.randrange(10)
print(f"My random number is {x}.")
print()

print("Here are some random numbers from 1 to 4...")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5))

print()

print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()

print("Will these next two random numbers be the same?")
a = random.randrange(10)
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")

# Q1: random.randrange(1, 5) produces numbers from 1 to 4.

# Q2: Using random.seed(400) makes the same sequence of random
# numbers appear each time the program runs.

# Q3: Changing the seed produces a different sequence, but that
# sequence repeats whenever the same seed is used again.

# Q4: Games can use seeds to recreate the same randomly generated
# world, map, or events. The same seed produces the same results.
