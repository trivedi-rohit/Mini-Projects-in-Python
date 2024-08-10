import os
bidder_info={}
end_of_bidding=False
def find_winner(bidder_details):
    highest_bid = 0
    winner=""
    for bidder in bidder_details:
        bidding_info = bidder_details[bidder]
        if bidding_info>highest_bid:
            highest_bid=bidding_info
            winner=bidder
    print(f"\nHere is the list of all bidders : {bidder_details}")
    print(f"\nThe winner is {winner} with a bid price of Rs. {highest_bid}.")

while not end_of_bidding:
    name = (input("Enter bidder name : "))
    bid = int(input("Enter your bidding price : "))
    bidder_info[name]=bid
    check = input("Is there any bidder? Type 'y' to add, else 'n' : ").lower()
    if check == 'n':
        end_of_bidding=True
        find_winner(bidder_info)
        break
    elif check=='y':
        os.system('cls')
