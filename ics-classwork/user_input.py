print("Enter the following information about an item you wish to purchase..")
print()

name = input("The name of the item: ")

price = float(input("The price: $"))

quantity = int(input("How many do you want? "))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

#Q1: price uses float(input(...)), so the prompt and input are on the same line and the input is converted to a decimal number. name originally used a separate print() and input(), and it stays as a string.
#Q3: A prompt is the message that tells the user what information to enter. If input() comes before the prompt, the program pauses without telling the user what to type, so it is confusing.
#Q4: int() converts input into a whole number, and float() converts input into a decimal number. input() by itself always returns a string. If you remove int() and float(), Python cannot correctly do the math with price and quantity.
