store = "No Frills"
item = "Apples"
price = 15
quantity = 300
subtotal = price * quantity 
tax = subtotal * 0.05 
total = tax + subtotal 


# f-string 
print(f"at {store} I bought some {item}.")

# concatenation 
print("They sold for $" + str(price) + " each.")

# dot format
print("I wanted to purchase {} of them.".format(quantity))

# f-string 
print(f"The total price, with tax included, was ${total}.")

# f-string
print(f"The tax is ${tax}.")

# f-string
print(f"The total price, with tax included, was ${total}.")