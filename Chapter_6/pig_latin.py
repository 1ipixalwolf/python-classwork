# # Assignment 11
# Pig Latin generator
# Haley Roveda 04/05/2024 

# have a function that translates words from English into Pig Latin. 
# Write a function called `pig_latin()` that accepts a word and return a modified version:
def translate(str):
    # If the word begins with a vowel (a, e, i, o, or u), add "way" to the end of the word
    if str[0] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o' or str[0] == 'u':
        newStr = str + 'way'
    # If the word begins with one consonant, move the consonant to the end and add "ay" after that.
    elif str[1] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o' or str[0] == 'u':
        newStr = str[1:] + str[0] + 'ay'
    # If the word begins with more than one consonant, move the first two consonants to the end and add "ay" after that.
    else:
        newStr = str[2:] + str[:2] + 'ay'
        
    return newStr
print(translate('cats'))
