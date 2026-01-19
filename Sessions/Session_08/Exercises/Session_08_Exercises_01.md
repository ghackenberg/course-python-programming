# Exercises 08: Advanced Data Structures & Algorithms

Welcome to the exercises for Session 08! This sheet covers fundamental data structures (Stacks, Queues, Linked Lists) and core algorithmic concepts (Recursion, Sorting).

## 8.1: Stacks and Queues

1.  **LIFO vs. FIFO:** Explain the difference between "Last-In, First-Out" and "First-In, First-Out". Provide one real-world example for each principle.
2.  **Stack Implementation:** Create a class `ActionHistory` that implements a Stack using a Python list. It should have methods `perform_action(action)` (push) and `undo_action()` (pop). Ensure `undo_action()` returns "Nothing to undo" if the stack is empty.
3.  **Queue Performance:** Why is using `list.pop(0)` for a queue considered inefficient in Python? Which class from the `collections` module should you use instead for high-performance queues?

## 8.2: Linked Lists

1.  **Memory Layout:** Describe how elements are stored in memory in a **Linked List** compared to a **Python List (Array)**.
2.  **The Node:** Write the Python code for a `Node` class that can be used in a singly linked list. Each node should store `data` and a reference to the `next` node.
3.  **Traversal:** Write a function `print_all_nodes(head)` that takes the head node of a linked list as input and prints the `data` of every node in the list until it reaches the end.

## 8.3: Recursion

1.  **The Base Case:** What is a "Base Case" in recursion, and why is it absolutely necessary for a recursive function to work correctly?
2.  **Recursive Calculation:** Write a recursive function `recursive_multiply(a, b)` that calculates the product of two positive integers `a` and `b` using only addition. 
    - *Hint:* $a \times b = a + (a \times (b - 1))$.
    - *Base Case:* If $b = 1$, the result is $a$.
3.  **The Call Stack:** Briefly explain what happens to the computer's memory (the Call Stack) when a recursive function calls itself many times without reaching a base case.

## 8.4: Basic Sorting Algorithms

1.  **Bubble Sort Logic:** In your own words, describe how the **Bubble Sort** algorithm moves the largest element to the end of a list during a single pass.
2.  **Algorithm Selection:** Which sorting algorithm (Bubble, Selection, or Insertion) is generally the most efficient for a list that is "almost sorted"?
3.  **Python's `sorted()`:** You have a list of tuples representing products: `products = [("Pump", 450), ("Belt", 50), ("Motor", 1200)]`. Use the `sorted()` function with a `lambda` as the `key` to sort these products by their **price** (the second element in each tuple) in ascending order.
