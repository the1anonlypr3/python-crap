import random

def diceroll():
    while True:
        sides = int(input("How many sides on the die? "))
        roll = random.randint(1, sides)
        print("You rolled a: " + str(roll))

diceroll()