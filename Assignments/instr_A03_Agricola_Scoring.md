# Assignment 03

Agricola is a board game about an unlikely subject: farming in the 17th century. The player start out in a small shack with their spouse and little else, but as the game progresses the player (hopefully) build up the farm into something that the player can look at with pride in the end. Players' final scores represent the quality of their farm, and the player with the best farm wins!

Agricola is one of my favorite games, but adding up all of the points at the end can be a little tedious. This assignment is to write a program that will allow the player to input information about the final state of the board and print the score.

For the purposes of this homework assignment, the code only has to calculate the score for the animals. (In the real game, the player also score for fields, pastures, grain, vegetables, rooms in the house, family members, and a few other categories.) The scoring break down for animals is as follows:

-   Sheep:

    -   -1 point for 0 sheep
    -   1 point for 1-3 sheep
    -   2 points for 4-5 sheep
    -   3 points for 6-7 sheep
    -   4 points for 8+ sheep

-   Wild boar:

    -   -1 point for 0 boar
    -   1 point for 1-2 boar
    -   2 points for 3-4 boar
    -   3 points for 5-6 boar
    -   4 points for 7+ boar

-   Cattle:
    -   -1 point for 0 cattle
    -   1 point for 1 cattle
    -   2 points for 2-3 cattle
    -   3 points for 4-5 cattle
    -   4 points for 6+ cattle.

Be sure to include comments in the code. At a minimum, the comment should include your name, date, course info and the purpose/description of the program at the top of the program file.

## Input

Your program should accept 3 integer inputs: the number of sheep, the number of wild boar, and the number of cattle.

## Output

Your program should output the phrase, "Your final score is xx points." where xx is the correct number of points.

## Sample execution

```output
How many sheep? 5
How many wild boar? 2
How many cattle? 3
Your final score is 5 points.
```
