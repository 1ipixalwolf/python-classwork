# Extra Credit 12

Watch this video on Sudoku: <https://youtu.be/G_UYXzGuqvM>. The video does cover the concepts of recursion (<https://www.geeksforgeeks.org/recursion/>) and backtracking (<https://www.geeksforgeeks.org/backtracking-algorithms/>), which are above and beyond this course.

The parts of this assignment:

Sudoku Solver \
The solver should be able to solve a Sudoku puzzle.
Just follow along with the code that is presented in the video.

Update the code to use a function so the program can call it multiple times with different starting puzzles to get a solution.

## Input

No inputs.

## Output

The code should display the initial board with blank spots.

Then the code should display the solution board with all spots filled out.

## For example

```output
 | | # | |3# |6| 
6| | #8| | #3| |4
 | |4#1| |5# |7| 
#################
1| |6#5|9| # | |2
9|7| # | |4# | |6
3| |2# | |8# | | 
#################
8| | # |5|1# | | 
 |2| # | | # | |7
5| | #3| | # | | 
```

The above board is a valid starting board with only one solution. Below are just the numbers, so you can use this if you desire.

```output
     3 6 
6  8  3 4
  41 5 7 
1 659   2
97   4  6
3 2  8   
8   51   
 2      7
5  3     
```

## Notes

The first part (Sudoku Solver) is provided for you in the video above.  Just use that as your starting point.
You are NOT making a full game here.  Just a solver.
