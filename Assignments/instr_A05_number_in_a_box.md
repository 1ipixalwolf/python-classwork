# Assignment 05

Write a function called `number_in_a_box()` that will accept a single integer as a parameter and print that number surrounded by a box of # characters. The box should always be three lines in height, and there should be one empty space on either side of the number.

Be sure to include comments in the code. At a minimum, the file should include your name, date, course info and the purpose/description of the program at the top of the program file.

## Examples

The following python code when run

```python
number_in_a_box(7)
```

should print:

```output
#####
# 7 #
#####
```

The following python code when run

```python
number_in_a_box(8008)
```

should print:

```output
########
# 8008 #
########
```

## HINTS

The `len()` function can find how many characters are in a string. For instance,

```python
word = 'test'
character_length = len(word)  # character_length = 4
```

would create an integer variable `character_length` with the value of 4.

Also, remember that the repetition operator (\*) can repeat a string several times.
