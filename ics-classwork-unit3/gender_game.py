gender = input("What is your gender (M or F): ")
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

if gender == "F" and age >= 20:
    married = input(f"Are you married, {first_name} (y or n)? ")

    if married == "y":
        print(f"Then I shall call you Mrs. {last_name}.")
    else:
        print(f"Then I shall call you Ms. {last_name}.")

if gender == "F" and age < 20:
    print(f"Then I shall call you {first_name} {last_name}.")

if gender == "M" and age >= 20:
    print(f"Then I shall call you Mr. {last_name}.")

if gender == "M" and age < 20:
    print(f"Then I shall call you {first_name} {last_name}.")
