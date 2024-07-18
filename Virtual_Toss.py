#Virtual Coin Toss for Cricket Match.
# Method -1 
import random
# ls = ["Heads","Tails"]
# ran = random.choice(ls)
# print(f"You Got a {ran}")

# Method -2
side =random.randint(0,1)
if side == 0:
    print ("Heads")
else:
    print("Tails")