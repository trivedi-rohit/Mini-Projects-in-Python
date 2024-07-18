need = input("Do you want pizza? (Y/N) : ")
if need == 'Y' or need == 'y':
    size = input("What size pizza you want? \n (Small/Medium/Large): ")
    if size == 'small' or size == "Small":
        bill = 100
    elif size == 'medium' or size == 'Medium':
        bill = 200
    elif size == 'large' or size == 'large':
        bill = 300
    pepper = input("Do you need pepperoni in your pizza? (Y/N) : ")
    if pepper == 'Y' or pepper == 'y':
        if size == 'small' or size == "Small":
            tb = bill + 30
        if (size == 'medium' or size == 'Medium') or (size == 'large' or size == 'large'):
            tb = bill + 50
    if pepper == 'n' or pepper == 'N':
            tb = bill
    cheese = input('Do you want to add cheese in pizaa? (Y/N) : ')
    if cheese == 'Y' or cheese == 'y':
        fb = tb + 20
        print(f"Your pizza cost you Rs. {fb}.\nEnjoy your pizza.")
    if cheese == 'n' or cheese == 'N':
        fb = tb
        print(f"Your pizza cost you Rs. {fb}.\nEnjoy your pizza.")
else:
    print("Thanks for visiting.")