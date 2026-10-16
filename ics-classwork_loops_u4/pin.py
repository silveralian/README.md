PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")

print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

# Q1: A while loop and an if statement both check a condition.
# If the condition is True, the indented code runs.

# Q2: An if statement checks once.
# A while loop keeps repeating while the condition is True.

# Q3: If PIN was an integer, entry would also need to be an integer:
# entry = int(input("ENTER YOUR PIN: "))

# Q4: If the input inside the while loop is removed, entry never changes.
# If the first PIN is wrong, the loop becomes an infinite loop.
