import random
import sys

def roll_dice(faces):
    return random.randint(1, faces)

faces = 6

print("Welcome to my dice simulator")
while True:
    print("Press enter to roll 1 die, or type the number of dice you want rolled. Type ""faces"" to enter the number of faces in each die.")
    roll = input().casefold()
    if roll == "faces":
        print("How many sides should each die have?")
        faces = input()
        while not faces.isnumeric():
            print("Please enter a valid number")
            faces = input()
        faces = int(faces)
    elif roll == "" or roll == "1":
        print("Rolling the dice")
        print("You rolled a", roll_dice(faces))
    elif roll.isnumeric():
        if int(roll) == 0:
            print("Please enter a valid input")
        else:
            roles = []
            for x in range(int(roll)):
                roles.append(roll_dice(faces))
            print("Rolling the dice")
            print("You rolled ", roles[0], end=", ")
            print(*roles[1:], sep=", ")
    else:
        print("Please enter a valid option")
    if roll == "quit":
        sys.exit()
