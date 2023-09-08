from replit import clear
from art import logo

print(logo)


# Initialize an empty dictionary
bids = {}
bidding_finished = False
bid_price_is_integer = True


def add_name_and_bid(bidder_name, bidder_price):
    bids[f"{bidder_name}"] = bidder_price 
    print(bids)
    return bids

def find_highest_bidder(bidding_record):
    # {"Angela": 123, "James": "321"}
    highest_bid = 0
    for bidder in bidding_record:
        # Save the value of bid to the variable bid amount
        bid_amount = bidding_record[bidder]
        bid_amount = int(bid_amount)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def check_bid_price(bid):
    if not bid.isnumeric():
        bid_price_is_integer = False
    return bid_price_is_integer

while not bidding_finished:
    name = input("What is your name?: \n")
    bid_price = input("What's your bid?: $")
    while not bid_price_is_integer:
        bid_price = input("What's your bid?: $")
        check_bid_price(bid_price)
    bidding_record = add_name_and_bid(name, bid_price)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    while should_continue != 'yes' and should_continue != 'no':
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == 'no':
        find_highest_bidder(bidding_record)
        bidding_finished = True
    elif should_continue == 'yes':
        #clear the console
        clear()

