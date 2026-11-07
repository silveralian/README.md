# 1.
# print(range(7)) shows: range(0, 7)
# print(list(range(7))) shows: [0, 1, 2, 3, 4, 5, 6]

# 2.
# "Hello" has 5 characters.
# range(len("Hello")) = range(5)
# The numbers are 0, 1, 2, 3, 4.

# 3.
# "box" has length 3.
# The last character "x" is at index 2.

message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at index 0 and is '{message[0]}'.")
print(f"The last character is at index {len(message) - 1} and is '{message[-1]}'.")

print()
print("Here are all the characters, one at a time:")
print()

vowels = 0

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

    if message[i] in "aAeEiIoOuU":
        vowels += 1

print()
print(f"Your message contains {vowels} vowels.")
