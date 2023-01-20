"""Checks light, if green, says go."""

light: str = input("What color is  the light?" )

if (light == "green"):
    print("Go yah slow poke!")
else:
    if (light != "red"):
        if (light == "yellow"):
            print("Slow down or speed up, choose your fate!")
        else:
            print("Go report this to the authorities!!!")
    else:
        print("Stop, or you will die!!")
print("Don't look at your phone.")
