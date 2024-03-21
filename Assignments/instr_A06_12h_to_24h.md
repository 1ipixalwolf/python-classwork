# Assignment 06

There are two common ways of recording time, 12 hour time and 24 hours time. In 12 hour time, we use AM to denote times before noon and PM to denote times after noon. In 24 hour time, we just keep counting until midnight. So 1 PM becomes 13:00, 2 PM is 14:00, etc.

Write a function named `convert_12_to_24()` that will accept an integer hour, an integer minute, and a string that is either AM or PM to indicate whether the time is before or after noon. It should return a string indicating a 24 hour time with the hour and minute separated by a colon.

Be sure to include comments in the code. At a minimum, the file should include your name, date, course info and the purpose/description of the program at the top of the program file.

## For Example

If the python code looks like this:

```python
print(convert_12_to_24(1, 15, 'PM'))
```

It should return something like this:

```output
13:15
```

Once again, the program should NOT have any input statements. It does not need to print results to the screen, merely return the newly created string. Remember that the program can use string concatenation (+) to join different values together into a single string.

## Test

I've included a few more test values below:

```python
print(convert_12_to_24(12, 30, 'AM'))    #  0:30
print(convert_12_to_24(12, 30, 'PM'))    # 12:30
print(convert_12_to_24(2, 30, 'AM'))     #  2:30
print(convert_12_to_24(4, 10, 'PM'))     # 16:10
```
