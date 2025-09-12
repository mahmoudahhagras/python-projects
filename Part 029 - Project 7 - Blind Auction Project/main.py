from art import logo
print(logo)
print("Welcome to the secret auction program.")
want = "yes" 
def auction():
    again = "yes"
    bids = {} 
    while again == "yes":
        name = input("What is your name?: ").lower()
        bid = int(input("What is your bid?: $"))
        bids[name] = bid
        again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if again == "no":
            highest_bid = 0
            winner = ""
            for bidder in bids:
                if bids[bidder] > highest_bid:
                    highest_bid = bids[bidder]
                    winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")

while want == "yes":
    auction()
    want = input("Want another auction? Type 'yes' or 'no'.\n").lower()
else:
    print("Goodbye!")