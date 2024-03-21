# Assignment 11

Be sure to include comments in the code. At a minimum, the file should include your name, date, course info and the purpose/description of the program at the top of the program file.

Write a program to do the following:

-   Concatenate two lists in the following order

    -   The function will input two lists and returns a list.

        ```python
        def concatenate_two_lists(list1, list2):
        ```

    -   Given:

        ```python
        list1 = ["Hello ", "take "]
        list2 = ["Dear", "Sir"]
        ```

    -   Output:

        ```output
        ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
        ```

-   Iterate both lists simultaneously

    Given two Python list, write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order. Assume both lists have the same number of items in them.

    -   The function will input two lists and returns a list.

        ```python
        def display_lists(list1, list2):
        ```

    -   Given:

        ```python
        list1 = [10, 20, 30, 40]
        list2 = [100, 200, 300, 400]
        ```

    -   Output:

        ```output
        10 400
        20 300
        30 200
        40 100
        ```

-   Remove all occurrences of a specific item from a list

    -   The function will input a remove value and a list and returns a list.

        ```python
        def remove_value_from_list(value, list):
        ```

    -   Given:

        ```python
        list1 = [5, 20, 15, 20, 25, 50, 20]
        ```

    -   Output:

        ```output
        [5, 15, 25, 50]
        ```
