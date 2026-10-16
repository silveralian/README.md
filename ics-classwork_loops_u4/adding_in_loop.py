print("I will add up the numbers you give me.")

total = 0

number = int(input("Number: "))

while number != 0:
    total += number

    print(f"The total so far is {total}")

    number = int(input("Number: "))

print()
print(f"The total is {total}.")
