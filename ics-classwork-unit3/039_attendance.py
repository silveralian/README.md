last_name = input("What's your last name? ")

if last_name <= "Carswell":
    print(f'You don\'t have to wait long, "{last_name}".')

elif last_name <= "Jones":
    print(f'That\'s not bad, "{last_name}".')

elif last_name <= "Smith":
    print(f'Looks like a bit of a wait, "{last_name}".')

elif last_name <= "Young":
    print(f'It\'s gonna be a while, "{last_name}".')

else:
    print(f'Not going anywhere for a while, "{last_name}"?')
