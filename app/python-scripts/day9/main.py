from replit import clear
from auction_art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}



def add_bidder(name, bid):
    bidders[name] = bid

def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

more_bidders=True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bidder(name, bid)
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "yes":
        clear()
    else:
        more_bidders = False
        find_highest_bidder(bidders)