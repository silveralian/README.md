import os
import time

frame = 0

while True:
    os.system("cls")

    animation_frame = frame % 8

    if animation_frame == 0:
        print("o...")
        print("....")

    elif animation_frame == 1:
        print(".o..")
        print("....")

    elif animation_frame == 2:
        print("..o.")
        print("....")

    elif animation_frame == 3:
        print("...o")
        print("....")

    elif animation_frame == 4:
        print("....")
        print("...o")

    elif animation_frame == 5:
        print("....")
        print("..o.")

    elif animation_frame == 6:
        print("....")
        print(".o..")

    elif animation_frame == 7:
        print("....")
        print("o...")

    frame += 1
    time.sleep(0.2)
