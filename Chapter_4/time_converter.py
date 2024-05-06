# Assignment 06
# Hayley Roveda 04/02/2024
# Convert 12 hour time to 24 hour time. Print the result. 

# a function named `convert_12_to_24()` that accepts an integer hour, an integer minute, and a string either AM or PM
def convert_12_to_24(a, b, c):
    if c == 'PM':
        a = a+12

    if a < 10:
        a = str(a)
        a = '0' + a

    if b < 10:
        b = str(b)
        b = '0' + b
    a = str(a)
    b = str(b)
    # return a string 24 hour time with hour : minute
    return a + ':' + b

print(convert_12_to_24(3, 8, 'AM'))