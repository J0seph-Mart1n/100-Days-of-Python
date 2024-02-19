#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to secret auction program.")
bidders = {}
bid = 0
while True:
    name = input("Enter your name: ")
    amount = int(input("Enter your amount: $"))
    next = input("Are there any other bidders. Type 'yes or 'no'.")
    bidders[name] = amount
    #clear()
    if next == "no":
        break

for key in bidders:
    if bidders[key] > bid:
        bid = bidders[key]
        max_bid_name = key

print(f"The winner is {max_bid_name} with a bid of {bid}")
