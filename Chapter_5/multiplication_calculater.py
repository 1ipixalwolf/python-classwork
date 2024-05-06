# Assignment 07
# Multiplication Calculator
# Haley Roveda 04/05/2024 
# accept 2 numbers as input and shows the result of multiplying them. 
# continue until the user enters 0 for both terms.

# output a greeting 
print("This program solves multiplication problems. Enter 0 for both terms to quit.")
while True:
    # accept 2 integers as input
    print("First number:")
    num1 = int(input())
    print("Second number:")
    num2 = int(input())
    # Display the result of the multiplication problem
    result = num1 * num2
    print(num1, 'x', num2, '=', result)
    # exit loop when both terns are 0
    if num1 == 0 and num2 == 0:
        break

# final Goodbye! message once the program is complete.
print('Goodbye!')
