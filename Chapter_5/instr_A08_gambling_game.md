# Assignment 08

Write a program that will simulate a simple gambling game with the following rules:

-   The player starts with $10.
-   The player rolls two dice and adds them together to get a total. (This can be done by generating two random numbers from 1-6.)
-   If the player rolls a 7, they gain $4.
-   If the player rolls any other number, they lose $1.

Your program should loop until the player is out of money. When it is done, it should display the following information to the screen:

-   The number of times the player rolled the dice.
-   The maximum amount of money the player had during the course of the game.

Be sure to include comments in the code. At a minimum, the file should include your name, date, course info and the purpose/description of the program at the top of the program file.

## Notes

Extra notes regarding this program:

-   Don't forget to use documentation and good variable names!
-   Even though I call this a game, there isn't any input or player interaction.
-   If the user uses a seed of 1, the program should produce the same numbers repeatedly. This will help with testing and making sure the values are correct.
-   The program should have variables to keep track of:
    -   the number of rolls
    -   the current total of money
    -   the max money
-   If the current total is ever greater than the max money, set the max money equal to the current total.
-   Investigate `randint()` function to generate the random dice throws

## Inputs

Ask the user for the seed to use for the random function.

## Outputs

The number of times the player rolled the dice.

The maximum amount of money the player had during the course of the game.

## Sample Output

```output
Enter seed: 1
You rolled 85 times before going broke.
The max value ever was 33 dollars.
```
