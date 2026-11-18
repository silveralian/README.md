import random 

list = [] 

while len(list) < 10:
    list.append(random.randint(1,100))

for n in range (len(list)):
    print(f"Slot {n} contains a {list[n]}")
