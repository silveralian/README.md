# 1. Changing n to another name still works.
# n is used because it stands for "number".

# 2. In range(0, 5), 0 is the starting number and 5 is the stopping number.
# 5 is not included.

# 3. The third number is the step.
# range(0, 5, 2) gives 0, 2, 4.

# 4. range(7) means 0, 1, 2, 3, 4, 5, 6.

# 5. range(3, 9) means 3, 4, 5, 6, 7, 8.

print("Type in a message, and I'll display it ten times.")
message = input("Message: ")

for n in range(2, 21, 2):
    print(f"{n}. {message}")
