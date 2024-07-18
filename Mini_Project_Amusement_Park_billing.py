# Billing for amusement park:
height = float(input('Enter you height (in feet) = '))
if height >= 4.5:
    age = int(input('Enter your age = '))
    if age <= 12:
        bill = 150
    elif age <= 18:
        bill = 250
    elif age <= 18 or age <= 60:
        bill = 500
    else:
        bill = 0 #! People above age 60 are not eligible due to health concerns.
        print("You are not not eligible for ride.")
    photo = (input("Do you want to take Photo also (Y/N)?"))
    if photo == "y" or photo == "Y":
        total_bill = bill + 50
        print(f'Final ticket price is Rs. {total_bill}.')
    else:
        print(f'Final ticket price is Rs. {bill}.')
else:
    print('You are not eligible for a ride now.')