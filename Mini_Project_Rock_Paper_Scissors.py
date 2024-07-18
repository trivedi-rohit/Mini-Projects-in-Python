# Game : "Rock Paper Scissors"
'''
#! Rules:
1. Rock wins against Scissors.
2. Scissors win against Paper.
3. Paper win against Rock.
'''
import random
print("Lets play Rock Paper Scissors game\n")
print("Rules:\n1. Rock wins against.\n2. Scissors win against Paper.\n3. Paper win against Rock.\n")
usr = int(input("0 for Rock.\n1 for Paper.\n2 for Scissors\nEnter the value from above choice :"))
comp = random.randint(0,2) 
print(f"System choice is : {comp}")
if usr == comp:
    print("Match is Draw.")
elif usr == 0:
    print("Your choice is Rock.")
    if (usr == 0 and comp == 1):
        print("You Loose.")
    elif (usr == 0 and comp == 2):
        print("You won the match.")
elif usr == 1:
    print("Your choice is Paper.")
    if (usr == 1 and comp == 0):
        print("You won the match.")
    elif (usr == 1 and comp == 2):
        print("You Loose.")
elif (usr == 2):
    print("Your choice is Scissors.")
    if (usr == 2 and comp == 0):
        print("You Loose.")
    elif (usr == 2 and comp == 1):
        print("You won the match.")
else:
    print("Number choosen is invalid.")