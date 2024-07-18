import random
target = random.randint(1, 100)

while True:
    userChoice = (input("Guess the targeted number or Quit(Q): "))
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success!! : you guessed correctly")
        break
    elif(userChoice < target):
        print("You gussed a smaller number. Take a bigger number.")
    else:
        print("Your guessed a was too big. Guess a smaller number.")
print("__________Game Over__________")