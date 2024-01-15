# Importing the 'os' module to clear the screen
import os

# Dictionary to store bidders' names and their bids
bids = {}

# Function to run the blind auction
def blind_auction():
    # Loop to get bids from participants
    while True:
        bidder_name = input("What's your name? ")
        bid_amount = int(input("What's your bid? $"))
        bids[bidder_name] = bid_amount
        # Clearing the console screen for privacy
        os.system('cls')
        more_bidders = input("Are there more bidders? (yes/no)").lower()
        if more_bidders == "no":
            break
    
    # Finding the highest bidder and announcing the winner
    highest_bidder = max(bids, key=bids.get)
    winning_bid = bids[highest_bidder] 
    print(f"The winner is {highest_bidder} with a bid of ${winning_bid}")

# Running the blind auction function to start the program
blind_auction()
