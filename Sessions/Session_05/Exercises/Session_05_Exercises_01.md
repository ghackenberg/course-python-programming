# Exercises 05: Error Handling & Debugging

Welcome to the exercises for Session 05! This sheet will help you practice identifying errors, handling exceptions gracefully, and debugging your code.

## 5.1: Types of Errors

Identify the type of error (Syntax, Runtime, or Logical) in the following scenarios. You don't need to write code for this, just analyze it.

1.  **Missing Parenthesis:** `print("Hello World"`
2.  **Wrong Formula:** `area = radius * 2` (when calculating the area of a square `radius ** 2`).
3.  **Invalid Conversion:** `value = int("ten")`.
4.  **Missing Colon:** `def my_func() print("Hi")`.
5.  **Off-By-One:** A loop intended to run 10 times only runs 9 times.
6.  **Missing Key:** `data = {"temp": 25.5}; print(data["humidity"])`.
7.  **Typo in Method:** `import math; print(math.calculat_sqrt(4))`.

## 5.2: Try-Except Blocks

1.  **Robust Input:**
    -   Write a script that asks the user for their age using `input()`.
    -   Use a `while` loop and a `try-except` block to keep asking until the user enters a valid integer.
    -   If they enter something that isn't a number, print "Invalid input. Please enter a number."

2.  **Safe List Access:**
    -   Create a list: `colors = ["red", "green", "blue"]`.
    -   Ask the user for an index (0-2).
    -   Use `try-except` blocks to handle:
        -   `IndexError`: If the user enters a number like 5. Print "Index out of range."
        -   `ValueError`: If the user enters a non-integer like "apple". Print "Please enter a valid integer."
    -   If the input is valid, print the color at that index.

3.  **File Recovery:**
    -   Try to open and read a file named `settings.conf`.
    -   Use a `try-except` block to catch `FileNotFoundError`.
    -   If the file doesn't exist, print "Settings file missing, loading defaults..." and create a dictionary `config = {"theme": "light", "volume": 50}`.
    -   If the file *does* exist (you can create it to test), read it and print "Settings loaded."

## 5.3: Raising Exceptions

1.  **Validation Function:**
    -   Write a function `calculate_speed(distance, time)` that returns `distance / time`.
    -   Inside the function, check if `time` is negative. If so, raise a `ValueError` with the message "Time cannot be negative."
    -   Check if `distance` is negative. If so, raise a `ValueError` with the message "Distance cannot be negative."
    -   Call the function with valid and invalid values inside a `try-except` block to test your error messages.

2.  **Inventory Check:**
    -   Write a function `remove_item(inventory, item)`. `inventory` is a list (e.g., `["apple", "banana"]`).
    -   If `item` is not in `inventory`, raise a `ValueError` with the message "Item not found in inventory".
    -   Otherwise, remove the item.
    -   Test the function with items that exist and items that don't.

## 5.4: Basic Debugging

1.  **Analyze the Bug:**
    -   Look at the code below. It is supposed to count down from 5 to 1, but it runs forever (infinite loop). Identify the error.
        ```python
        n = 5
        while n > 0:
            print(n)
            n + 1 # Error is here
        ```
    -   Fix the code so it counts down correctly.

2.  **Trace the Logic:**
    -   Manually trace the values of `a` and `b` in the following snippet. What are their values at the end?
        ```python
        a = 10
        b = 5
        if a > b:
            a = a - 2
        else:
            b = b - 2
        ```
    -   Write the final values of `a` and `b` as a comment or print them to verify.
