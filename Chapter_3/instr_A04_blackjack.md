# Assignment 04

In the game of blackjack, the player is dealt two cards. The total value of the cards is determined by their rank - numeric cards are worth the number on the card, face cards (Jack, Queen, and King) are worth 10, and aces are worth either 1 or 11 (for the purposes of this program, assume aces are equal to 11). The player decides whether they want to ask for additional cards (being dealt another card is know as a hit); the goal of the game is to get as close to 21 as possible without going over.

In addition to the basic rules, the player can choose to split their hand (double the bet and play each card separately) if the player is dealt two of the same card. There is some nuance to how splitting should be played, but the program should always split if the player is dealt two aces or two eights.

Write a program that will ask the user to input the value of two cards. The valid values are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.

If the player is dealt two aces or two eights, **print "Split"**

If the value of the player's cards adds up to 21, **print "Blackjack!"**

If the value of the player's cards adds up to 17 - 20, print "Stay". Exception: if the total is 17 and one of the cards is an ace, **print "Hit"**

If the value of the player's cards adds up to less than or equal to 16, **print "Hit"**

Be sure to include comments in the code. At a minimum, the file should include your name, date, course info and the purpose/description of the program at the top of the program file.

## Input

Two strings representing the cards the player is dealt.

## Output

One of the following options: Split, Blackjack!, Stay, or Deal

## Sample Executions 1

```output
Card one: A
Card two: 10
Blackjack!
```

## Sample Executions 2

```output
Card one: 4
Card two: 5
Hit
```

## Sample Executions 3

```output
Card one: 8
Card two: 8
Split
```

## Sample Executions 4

```output
Card one: 7
Card two: K
Stay
```