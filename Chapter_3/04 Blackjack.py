# Assignment 04 Blackjack
# Hayley Roveda 03/25/2024
# user is dealt two cards. Their value is their rank - numeric cards = their number, Jack, Queen, and King = 10, and aces = 11. user decides whether they want to ask for additional cards know as a hit; the goal of the game is to get as close to 21 as possible without going over.
# user can choose to split their hand (double the bet and play each card separately) if user is dealt two of the same card. the program should always split if user is dealt two aces or two eights.

# ask user to input the value of two cards. valid values: A, 2-10, J, Q, or K.
print("Type a number 2-10, A, J, Q, or K")
card1 = input()
if card1 == "A":
    card1 = 11
if card1 == "J":
    card1 = 10
if card1 == "K":
    card1 = 10
if card1 == "Q":
    card1 = 10

print("Type a number 2-10, A, J, Q, or K")
card2 = input()
if card2 == "A":
    card2 = 11
if card2 == "J":
    card2 = 10
if card2 == "K":
    card2 = 10
if card2 == "Q":
    card2 = 10

# If user is dealt two aces or two 8s, **print("Split")**
if card1 == 8 and card2 == 8:
    print("Split")

if card1 == 11 and card2 == 11:
    print("Split")

combow = card1 + card2
# If the value of the user's cards adds up to 21, **print("Blackjack!")**
if combow == 21:
    print("Blackjack!")
# If the value of the user's cards adds up to 17 - 20, print("Stay") Exception: if the total is 17 and one of the cards is an ace, **print("Hit")**

# If the value of the user's cards adds up to <= 16, **print("Hit")**
