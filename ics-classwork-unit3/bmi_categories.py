height = float(input("Your height in meters: "))
weight = float(input("Your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

print(f"BMI Category: {category}")
