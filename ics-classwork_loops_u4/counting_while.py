print("Type in a message, and I'll display it several times.")

message = input("Message: ")
print()

times = int(input("How many times? "))
print()

n = 0

while n < times:
    print(f"{(n + 1) * 10}. {message}")
    n += 1

# n += 1 adds 1 to n every time the loop repeats.
# Without it, n never changes and the loop becomes infinite.
