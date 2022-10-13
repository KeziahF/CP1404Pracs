COLOUR_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}

colour = input("Enter colour name: ").lower()

while colour != "":
    if colour in COLOUR_TO_HEX.keys():
        print(COLOUR_TO_HEX[colour])
    else:
        print("invalid input")
    colour = input("Enter colour name: ").lower()