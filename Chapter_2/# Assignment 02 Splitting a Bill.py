# Assignment 02 Splitting a Bill
# Hayley Roveda 03/23/2024
# Calculate how much each person should pay to evenly split the bill. 

# take user input of the bill, tip, and number of people 
print("The bill?")
bill = float(input())
print("Percentage to tip? (as a percentage, not a decimal)")
tip_percent = int(input())
tip = bill*(tip_percent/100)
print("Number of people splitting the bill?")
people = int(input())

# Calculate individual contributions
contribution = (bill+tip)/people
round_contribution = round(contribution, 2)
# print a message indicating how much each person should pay.
print("Each person should pay $" round_contribution)