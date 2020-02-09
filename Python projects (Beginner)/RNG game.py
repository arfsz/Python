import random

x = random.randrange(1 , 20)

ask = ""

while ask != x:
    ask = int(input("Guess a number from 1-20:"))
    if ask > x:
        print("Number too high.")
    elif ask < x:
        print("Number too low.")

if ask == x:
    print("Congratiualtions! You guessed the number correctly!")
    
