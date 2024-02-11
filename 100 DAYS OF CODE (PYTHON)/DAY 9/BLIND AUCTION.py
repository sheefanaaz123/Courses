import os 

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    try:
        price = int(input("What is your bid?: $"))
        if price <= 0:
            print("Please enter a positive bid amount.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for your bid.")
        continue

    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

    elif should_continue == "yes":
        clear_screen()  

def clear_screen():
    if os.name == "nt":  
        os.system("cls")
    else: 
        os.system("clear")
