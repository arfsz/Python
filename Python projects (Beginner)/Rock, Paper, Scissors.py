import random

r = "rock"
p = "paper"
s = "scissors"

x = random.choice([r, p, s])

ask = input("Choose Rock or Paper or Scissors (no capital letters): ")

if ask == r and x == s or ask == s and x == p or ask == p and x == r:
    print("Congrats!! You Win!")
else:
    print("Sorry.. You lose... Try again")
