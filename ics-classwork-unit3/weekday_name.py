number = int(input("Enter a number from 0 to 7: "))

if number == 1:
    day = "Monday"
elif number == 2:
    day = "Tuesday"
elif number == 3:
    day = "Wednesday"
elif number == 4:
    day = "Thursday"
elif number == 5:
    day = "Friday"
elif number == 6:
    day = "Saturday"
elif number == 7 or number == 0:
    day = "Sunday"
else:
    day = "Error"

print(day)
