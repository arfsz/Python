import random

def Dice_roll():
    x = random.randrange(1 ,6)
    return x

ask = "y"

while ask == "y":
    print(Dice_roll())
    ask = input("Want to spin again? (y/n)")
