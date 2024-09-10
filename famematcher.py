print("Famematcher")
gender = input("Enter your gender:")
if gender == "male":
    haircolor = input("Enter your hair color:")
    if haircolor == "brown":
        eye_color = input("Enter your eye color:")
        if eye_color == "brown":
            print("Your match is Daniel Radcliff")
            print("Or Robert Downey jr")
        else:
            print("No match, try checking your input")
    elif haircolor == "red":
        eye_color = input("Enter your eye color:")
        if eye_color == "blue":
            print("Your match is Rupert Grint")
        else:
            print("No match, try checking your input")
    elif haircolor == "blonde":
        eye_color = input("Enter your eye color:")
        if eye_color == "blue":
            print("Your match is Chris Hemsworth")
        else:
            print("No match, try checking your input")
    elif haircolor == "none":
        eye_color = input("Enter your eye color:")
        if eye_color == "brown":
            print("Your match is The Rock")
        else:
            print("No match, try checking your input")
    else:
        print("Invalid haircolor, try brown, blonde, none or red")
elif gender == "female":
    haircolor = input("Enter your hair color:")
    if haircolor == "brown":
        eye_color = input("Enter your eye color:")
        if eye_color == "brown":
            print("Your match is Emma Watson")
            print("Or Selena Gomez")
        else:
            print("No match, try checking your input")
    elif haircolor == "blonde":
        eye_color = input("Enter your eye color:")
        if eye_color == "blue":
            print("Your match is Laurie Holden")
        elif eye_color == "brown":
            print("Your match is Jennifer Lawrence")
        else:
            print("No match, try checking your input")
    else:
        print("invalid hair color, try blonde or brown")
else:
    print("Invalid gender, try male or female")
    