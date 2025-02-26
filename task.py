print("Hi! Welcome to the Silent Auction house program! \n"
      "Let's bid!")

bids = {}
ordered_bids = {}
def add_bid(bid_list, name, bid):
    bid_list[name]=bid
    bid_list = dict(sorted(bid_list.items(), key=lambda item: item[1], reverse=True))

choice = 1
while choice != 0:
    bidder = str(input("What's your name?"))
    bid = input("What's your bid?")
    add_bid(bids, bidder, bid)
    print("Bid computed!\nType 0 to end program \nor anything else to add more bids.\n ")
    choice = int(input("Your input: "))

highest_bid = next(iter(bids.items()))
print(f"The winner is {highest_bid[0]}, for ${highest_bid[1]}!\nCongratulations! ")
