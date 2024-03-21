# Assignment 10

Write a program to prompt for a file name, and then read through the file and look for lines of the form:

> X-DSPAM-Confidence: 0.8475

When the program encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When the program reaches the end of the file, print out the average spam confidence.

Be sure to include comments in the code. At a minimum, the file should include your name, date, course info and the purpose/description of the program at the top of the program file.

## Example Output

```outout
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
```

```output
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
```

## Notes

Test the program on the mbox.txt and mbox-short.txt files.

-   [www.py4e.com/code3/mbox.txt](https://www.py4e.com/code3/mbox.txt)
-   [www.py4e.com/code3/mbox-short.txt](https://www.py4e.com/code3/mbox-short.txt)
