PIN = "12345"
MAX_TRIES = 4

tries = 0

print("WELCOME TO THE BANK OF GALLO.")

entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < MAX_TRIES:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

elif tries >= MAX_TRIES:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")
