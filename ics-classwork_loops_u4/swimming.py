current_temperature = float(input("What is the current water temperature? "))

minimum_temperature = 79
saved_temperature = current_temperature

swimmer1 = "GALLANT"
swimmer2 = "GOOFUS"

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer1} approaches the lake....")

swim_time = 0

# Pre-test loop
while current_temperature >= minimum_temperature:
    swim_time += 1
    print(f"\t{swimmer1} swims for a bit. Swim time: {swim_time} min.")

    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")

print(f"{swimmer1} stops swimming. Total swim time: {swim_time} min.")

# Reset the temperature
current_temperature = saved_temperature

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer2} approaches the lake....")

swim_time = 0

# Post-test loop
while True:
    swim_time += 1
    print(f"\t{swimmer2} swims for a bit. Swim time: {swim_time} min.")

    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")

    if current_temperature < minimum_temperature:
        break

print(f"{swimmer2} stops swimming. Total swim time: {swim_time} min.")

# Q1: At 80.5 F, Goofus and Gallant both swim for 4 minutes.
# Q2: At 78 F, Gallant does not swim, but Goofus swims for 1 minute.
# Q3: Gallant checks the water temperature before swimming.
# Q4: Goofus dives in first and checks the temperature afterward.
# Q5: The first while loop checks before running. The second runs first
# and uses break to leave the loop when the water is too cold.
# Q6: The first loop is a pre-test loop. The second is a post-test loop.
