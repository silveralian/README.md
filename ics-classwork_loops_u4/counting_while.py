print("Type in a message, and I'll display it twenty times.")

message = input("Message: ")
print()

n = 0
while n < 100:
    print(f"{n + 10}. {message}")
    n += 10
