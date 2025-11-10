---
marp: true
theme: fhooe
header: Introduction to Python & Programming Basics
footer: Dr. Georg Hackenberg, Professor for Computer Science and Industrial Systems
paginate: true
math: mathjax
---

<!-- Abstract illustration of interconnected nodes and lines representing programming concepts, with a glowing Python logo subtly integrated, all set against a dark, swirling galaxy background. The overall aesthetic is futuristic and conceptual. -->

![bg right](./Images/Chapter.jpg)

# Chapter 1: Introduction to Python & Programming Basics

This chapter includes the following sections:

- 1.1: What is Programming?
- 1.2: Why Python?
- 1.3: Setting up Your Environment
- 1.4: Basic Syntax: Variables and Data Types
- 1.5: Input and Output

---

<!-- Abstract illustration of a human hand interacting with lines of code and binary data, symbolizing the act of programming, set against a dark galaxy background with subtle light trails. -->

![bg right](./Images/Section_1.jpg)

## 1.1: What is Programming?

This section includes the following content:

- What is Programming?
- What Programmers Do
- Algorithms and Logic
- Machine Code vs. High-Level Languages
- Interpreted vs. Compiled Languages
- Why Learn Programming?
- Problem-Solving Approach
- Example: Simple Instructions

---

<div class="columns">
<div class="two">

### What is Programming?

- **Definition:** Giving instructions to a computer to perform a task.
- **Goal:** Automate tasks, solve problems, create applications.
- **Language:** Computers understand machine code (binary). We use high-level languages (like Python) that are translated.

**Illustration:**

![Diagram illustrating the concept of programming, showing a human giving instructions to a computer, which then executes tasks. (Mermaid.js)](./Diagrams/Mermaid/programming_concept.svg)

---

<div class="columns">
<div class="two">

### What Programmers Do

- **Analyze:** Understand the problem.
- **Design:** Plan the solution (algorithm).
- **Code:** Write instructions in a programming language.
- **Test:** Check if the solution works correctly.
- **Debug:** Fix errors.
- **Deploy:** Make the solution available.

**Illustration:**

![Flowchart depicting the typical workflow of a programmer: Analyze -> Design -> Code -> Test -> Debug -> Deploy. (Mermaid.js)](./Diagrams/Mermaid/programmer_workflow.svg)

---

<div class="columns">
<div class="two">

### Algorithms and Logic

- **Algorithm:** A step-by-step procedure for solving a problem.
- **Logic:** The reasoning behind the steps.
- **Example:** Recipe for baking a cake is an algorithm.

</div>
<div class="two">

```
Algorithm: Make Coffee
1. Get water
2. Heat water
3. Add coffee grounds
4. Pour water over grounds
5. Serve
```

</div>
</div>

---

<div class="columns">
<div class="three">

### Machine Code vs. High-Level Languages

- **Machine Code:** Binary instructions (0s and 1s) directly understood by the CPU.
- **High-Level Languages:** Human-readable languages (Python, Java, C++).
- **Translators:**
    - **Compilers:** Translate entire program before execution.
    - **Interpreters:** Translate and execute line by line.

</div>
<div>

![Diagram showing the hierarchy from high-level languages to machine code, with an interpreter/compiler in between. (Mermaid.js)](./Diagrams/Mermaid/language_levels.svg)

</div>
</div>

---

<div class="columns">
<div class="two">

### Interpreted vs. Compiled Languages

- **Interpreted (e.g., Python):**
    - Code executed line by line.
    - Easier debugging.
    - Slower execution.
    - More flexible.
- **Compiled (e.g., C++):**
    - Code translated entirely to machine code first.
    - Faster execution.
    - Harder debugging.
    - Less flexible.

</div>
<div class="three">

![Comparison diagram illustrating how an interpreter executes code line by line versus how a compiler translates the entire code before execution. (Mermaid.js)](./Diagrams/Mermaid/interpreter.svg)

![Comparison diagram illustrating how an interpreter executes code line by line versus how a compiler translates the entire code before execution. (Mermaid.js)](./Diagrams/Mermaid/compiler.svg)

</div>
</div>

---

<div class="columns">
<div>

### Why Learn Programming?

- **Problem Solving:** Develop logical thinking.
- **Automation:** Make computers do repetitive tasks.
- **Creativity:** Build new tools and applications.
- **Career Opportunities:** High demand in many fields.
- **Understanding Technology:** Demystify how software works.

</div>
<div class="two">

![Icon-based diagram showing the benefits of learning programming: Problem Solving, Automation, Creativity, Career Opportunities, Understanding Technology. (Tikz) width:1000px](./Diagrams/Tikz/benefits_programming.tikz.svg)

</div>
</div>

---

<div class="columns">
<div class="three">

### Problem-Solving Approach

1.  **Understand the Problem:** What needs to be solved?
2.  **Break Down:** Divide into smaller, manageable parts.
3.  **Plan:** Devise a step-by-step solution (algorithm).
4.  **Implement:** Write the code.
5.  **Test & Refine:** Verify and improve.

</div>
<div>

![Numbered list or flowchart illustrating the problem-solving approach: Understand -> Break Down -> Plan -> Implement -> Test & Refine. (Mermaid.js)](./Diagrams/Mermaid/problem_solving_steps.svg)

</div>
</div>

---

<div class="columns">
<div class="two">

### Example: Simple Instructions

- **Task:** Calculate the sum of two numbers.
- **Algorithm:**
    1.  Get the first number.
    2.  Get the second number.
    3.  Add them together.
    4.  Display the result.

</div>
<div class="two">

```python
# Python example
num1 = 10
num2 = 20
sum_result = num1 + num2
print(sum_result) # Output: 30
```

</div>
</div>

---

<!-- Abstract illustration highlighting Python's versatility with various icons (web, data science, AI, automation) emerging from a central, glowing Python logo, all against a dark galaxy backdrop. -->

![bg right](./Images/Section_2.jpg)

## 1.2: Why Python?

This section includes the following content:

- Readability and Simplicity
- Versatility
- Large Community and Libraries
- Cross-Platform Compatibility
- High Demand in Industry
- Comparison with Other Languages (Briefly)
- Python's Philosophy (Zen of Python)
- Example: "Hello, World!" in Python

---

<div class="columns">
<div class="two">

### Readability and Simplicity

- **English-like Syntax:** Easy to read and understand.
- **Less Boilerplate:** Write more with fewer lines of code.
- **Indentation:** Enforces clean and consistent code structure.

</div>
<div class="two">

*Python*

```python
# Python
if x > 0:
    print("Positive")
```

*Java*

```java
// Java
if (x > 0) {
    System.out.println("Positive");
}
```

</div>
</div>

---

<div class="columns">
<div>

### Versatility

- **Web Development:** Django, Flask
- **Data Science & AI:** NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch
- **Automation & Scripting:** System administration, task automation
- **Desktop Applications:** PyQt, Kivy
- **Game Development:** Pygame

</div>
<div class="two">

![Icon-based diagram showing various applications of Python: Web Development, Data Science & AI, Automation & Scripting, Desktop Applications, Game Development. (Tikz) width:1000px](./Diagrams/Tikz/python_applications.tikz.svg)

</div>
</div>

---

<div class="columns">
<div class="two">

### Large Community and Libraries

- **Vibrant Community:** Extensive support, tutorials, forums.
- **Rich Ecosystem:** Thousands of third-party libraries (PyPI).
- **"Batteries Included":** Standard library covers many common tasks.

</div>
<div class="two">

![Diagram representing a large, active community, possibly with interconnected nodes or a crowd of people, symbolizing support, libraries, and ecosystem. (Mermaid.js)](./Diagrams/Mermaid/python_community.svg)

</div>
</div>

---

<div class="columns">
<div class="two">

### Cross-Platform Compatibility

- **Write Once, Run Anywhere:** Python code runs on:
    - Windows
    - macOS
    - Linux
    - And many other platforms
- No need to recompile for different operating systems.

</div>
<div class="two">

![Diagram showing Python code running on different operating systems (Windows, macOS, Linux) with a single codebase. (Mermaid.js)](./Diagrams/Mermaid/cross_platform.svg)

</div>
</div>

---

<div class="columns">
<div class="two">

### High Demand in Industry

- **Top Programming Language:** Consistently ranks among the most popular.
- **Job Market:** High demand for Python developers in various sectors.
- **Companies Using Python:** Google, Instagram, Spotify, Netflix, NASA.

</div>
<div class="two">

![Chart or infographic indicating the high demand for Python developers, possibly with growth trends or company logos. (Tikz) width:1000px](./Diagrams/Tikz/python_job_market.tikz.svg)

</div>
</div>

---

### Comparison with Other Languages (Briefly)

| Language   | Key Characteristics                     | Primary Use Cases                               |
| :--------- | :-------------------------------------- | :---------------------------------------------- |
| **Python** | General-purpose, easy to read           | Web, Data Science, AI, Automation               |
| **Java**   | Statically typed, fast                  | Enterprise Apps, Android                        |
| **JavaScript** | Primarily for web frontend, asynchronous | Web Frontend, Backend (Node.js)                 |
| **C++**    | High performance, system-level          | Game Dev, OS, Embedded Systems                  |

---

<div class="columns">
<div class="two">

### Python's Philosophy (Zen of Python)

- **`import this`:** Reveals 19 guiding principles.
- **Key Principles:**
    - Beautiful is better than ugly.
    - Explicit is better than implicit.
    - Simple is better than complex.
    - Readability counts.

</div>
<div class="two">

```python
import this
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Example: "Hello, World!" in Python

- The classic first program.
- Demonstrates basic output.
- Simple and straightforward.

</div>
<div class="two">

```python
print("Hello, World!")
```

</div>
</div>

---

<!-- Abstract illustration of a developer's workstation with glowing screens displaying code and terminal windows, surrounded by floating virtual environment symbols, set against a dark galaxy background. -->

![bg right](./Images/Section_3.jpg)

## 1.3: Setting up Your Environment

This section includes the following content:

- Python Installation
- IDE/Editor Choices
- Virtual Environments (venv)
- Running Python Scripts from Terminal
- Interactive Mode (REPL)
- Basic VS Code Setup for Python
- First Script Execution
- Troubleshooting Common Setup Issues

---

<div class="columns">
<div class="two">

### Python Installation

- **Official Website:** `python.org/downloads`
- **Choose Version:** Latest stable version (e.g., Python 3.x).
- **Important:** Check "Add Python to PATH" during installation on Windows.
- **Verify:** Open terminal/command prompt and type `python --version`.

</div>
<div class="two">

![Screenshot or stylized representation of the official Python download page on python.org. (Diffusion Model)](./Images/Python_Download.jpg)

</div>
</div>

---

<div class="columns">
<div class="two">

### IDE/Editor Choices

- **Integrated Development Environment (IDE):**
    - **PyCharm:** Full-featured, powerful (Community Edition is free).
    - **VS Code:** Lightweight, highly customizable with extensions.
- **Text Editors:**
    - Sublime Text, Atom (less features, more basic).

</div>
<div class="two">

Visual Studio Code

![The official logo of Visual Studio Code. (Existing SVG) width:130px](https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg)

*PyCharm*

![The official logo of PyCharm. (Existing SVG) width:1000px](https://upload.wikimedia.org/wikipedia/commons/5/5d/JetBrains_PyCharm_Product_Logo.svg)

</div>
</div>

---

<div class="columns">
<div class="two">

### Virtual Environments (venv)

- **Purpose:** Isolate project dependencies.
- **Avoids Conflicts:** Different projects can use different library versions.
- **Creation:** `python -m venv myenv`
- **Activation:**
    - Windows: `.\myenv\Scripts\activate`
    - macOS/Linux: `source myenv/bin/activate`

</div>
<div class="two">

```bash
# Create
python -m venv myproject_env

# Activate (Windows)
.\myproject_env\Scripts\activate

# Activate (macOS/Linux)
source myproject_env/bin/activate
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Running Python Scripts from Terminal

- **Save File:** Create a file named `my_script.py`.
- **Navigate:** Open terminal in the directory where `my_script.py` is saved.
- **Execute:** `python my_script.py`

</div>
<div class="two">

```python
# my_script.py
print("This is my first script!")
```

```bash
# Terminal
python my_script.py
# Output: This is my first script!
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Interactive Mode (REPL)

- **REPL:** Read-Eval-Print Loop.
- **Purpose:** Experiment with code snippets, test ideas quickly.
- **Launch:** Type `python` in your terminal.
- **Exit:** `exit()` or `Ctrl+Z` (Windows) / `Ctrl+D` (macOS/Linux).

</div>
<div class="two">

```python
>>> 2 + 2
4
>>> "hello" + " world"
'hello world'
>>> x = 10
>>> x * 5
50
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Basic VS Code Setup for Python

- **Install Python Extension:** From VS Code Marketplace.
- **Select Interpreter:** `Ctrl+Shift+P` -> "Python: Select Interpreter".
- **Run & Debug:** Use the "Run" button or `F5`.
- **Integrated Terminal:** `Ctrl+` ` (backtick).

</div>
<div class="two">

![Screenshot or stylized representation of the Python extension page in VS Code Marketplace. (Diffusion Model)](./Images/VS_Code_Python_Extension.jpg)

</div>
</div>

---

<div class="columns">
<div class="two">

### First Script Execution

- **Create `hello.py`:**
    ```python
    print("Hello, Python Course!")
    ```
- **Open Terminal:** Navigate to the folder.
- **Run:** `python hello.py`
- **Expected Output:** `Hello, Python Course!`

</div>
<div class="two">

```bash
# Terminal
cd my_project_folder
python hello.py
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Troubleshooting Common Setup Issues

- **`'python' is not recognized`:** Python not added to PATH.
- **Module Not Found Error:** Not in correct virtual environment or module not installed.
- **Syntax Errors:** Typos, incorrect indentation.
- **Solution:** Double-check installation, activate venv, read error messages carefully.

</div>
<div>

![Icon or diagram representing troubleshooting, possibly a wrench, a magnifying glass, or a person looking at an error message. (Tikz) width:1000px](./Diagrams/Tikz/troubleshooting.tikz.svg)

</div>
</div>

---

<!-- Abstract illustration of glowing data structures (integers, floats, strings, booleans) flowing and connecting, representing variables and data types, against a dark galaxy background. -->

![bg right](./Images/Section_4.jpg)

## 1.4: Basic Syntax: Variables and Data Types

This section includes the following content:

- Comments
- Variables: Naming Rules, Assignment
- Basic Data Types: Integers, Floats, Strings, Booleans
- Type Checking (`type()`)
- Type Conversion (`int()`, `str()`, `float()`)
- Operators: Arithmetic, Assignment, Precedence

---

<div class="columns">
<div class="two">

### Comments

- **Purpose:** Explain code, make it readable for humans.
- **Ignored by Interpreter:** Not executed as part of the program.
- **Single-line:** Start with `#`.
- **Multi-line (Docstrings):** Enclosed in triple quotes (`"""Docstring"""`).

</div>
<div class="two">

```python
# This is a single-line comment

"""
This is a multi-line comment
or a docstring.
"""
x = 10 # Inline comment
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Variables: Naming Rules, Assignment

- **Variables:** Named storage locations for data.
- **Naming Rules:**
    - Start with letter or underscore (`_`).
    - Can contain letters, numbers, underscores.
    - Case-sensitive (`age` is different from `Age`).
    - Cannot be Python keywords (e.g., `if`, `for`).
- **Assignment:** Use `=` operator.

</div>
<div class="two">

```python
name = "Alice"
age = 30
_private_var = "secret"
my_variable_1 = 100
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Basic Data Types: Integers, Floats, Strings, Booleans

- **Integers (`int`):** Whole numbers (e.g., `5`, `-100`).
- **Floats (`float`):** Decimal numbers (e.g., `3.14`, `-0.5`).
- **Strings (`str`):** Text, enclosed in quotes (e.g., `"hello"`, `'Python'`).
- **Booleans (`bool`):** `True` or `False`.

</div>
<div class="two">

```python
my_int = 10
my_float = 3.14
my_string = "Hello"
my_bool = True
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Type Checking (type())

- **Function:** `type()`
- **Purpose:** Determine the data type of a variable or value.
- **Useful for:** Debugging, understanding variable behavior.

</div>
<div class="two">

```python
num = 10
text = "Python"
is_active = True

print(type(num))      # <class 'int'>
print(type(text))     # <class 'str'>
print(type(is_active))# <class 'bool'>
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Type Conversion (int(), str(), float())

- **Purpose:** Convert a value from one data type to another.
- **Functions:**
    - `int()`: Converts to integer.
    - `float()`: Converts to float.
    - `str()`: Converts to string.
- **Caution:** Not all conversions are possible (e.g., `"hello"` to `int`).

</div>
<div class="two">

```python
num_str = "123"
num_int = int(num_str) # 123 (int)

float_num = 3.14
float_str = str(float_num) # "3.14" (str)

int_val = 5
int_float = float(int_val) # 5.0 (float)
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Operators: Arithmetic

- **Addition:** `+`
- **Subtraction:** `-`
- **Multiplication:** `*`
- **Division:** `/` (float result)
- **Floor Division:** `//` (integer result)
- **Modulo:** `%` (remainder)
- **Exponentiation:** `**`

</div>
<div class="two">

```python
print(10 + 3)  # 13
print(10 - 3)  # 7
print(10 * 3)  # 30
print(10 / 3)  # 3.333...
print(10 // 3) # 3
print(10 % 3)  # 1
print(2 ** 3)  # 8
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Operators: Assignment

- **Assignment:** `=`
- **Add and Assign:** `+=` (e.g., `x += 1` is `x = x + 1`)
- **Subtract and Assign:** `-=`
- **Multiply and Assign:** `*=`
- **Divide and Assign:** `/=`
- **Other:** `//=`, `%=`, `**=`

</div>
<div class="two">

```python
x = 5
x += 2 # x is now 7
y = 10
y *= 3 # y is now 30
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Operator Precedence

- **Order of Operations:** Which operations are performed first.
- **PEMDAS/BODMAS:** Parentheses/Brackets, Exponents/Orders, Multiplication/Division, Addition/Subtraction.
- **Python follows standard mathematical precedence.**
- Use parentheses `()` to explicitly control order.

</div>
<div class="two">

```python
result1 = 10 + 5 * 2   # 10 + 10 = 20
result2 = (10 + 5) * 2 # 15 * 2 = 30
print(result1) # 20
print(result2) # 30
```

</div>
</div>

---

<!-- Abstract illustration of data flowing into and out of a central processing unit, depicted as glowing streams of information, symbolizing input and output operations, against a dark galaxy background. -->

![bg right](./Images/Section_5.jpg)

## 1.5: Input and Output

This section includes the following content:

- `print()` function: Basics
- `print()` with multiple arguments, `sep`, `end`
- Formatted Output (f-strings, `.format()`)
- `input()` function: Getting User Input
- Input Type Conversion
- Combining Input and Output
- Example: Simple Interactive Program
- Practice Exercise

---

<div class="columns">
<div class="two">

### `print()` function: Basics

- **Purpose:** Display output to the console.
- **Syntax:** `print(value1, value2, ...)`
- **Default Behavior:** Prints values separated by a space, ends with a newline.

</div>
<div class="two">

```python
print("Hello")
print("World")
# Output:
# Hello
# World

print("Hello", "World")
# Output: Hello World
```

</div>
</div>

---

<div class="columns">
<div class="two">

### `print()` with multiple arguments, `sep`, `end`

- **`sep` (separator):** Specifies how to separate arguments (default is space).
- **`end` (end character):** Specifies what to print at the end (default is newline `\n`).

</div>
<div class="two">

```python
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print("Loading", end="...")
print("Done!")
# Output: Loading...Done!
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Formatted Output (f-strings, `.format()`)

- **f-strings (Formatted String Literals):** (Python 3.6+)
    - Prefix string with `f`.
    - Embed expressions inside `{}`.
- **`.format()` method:** Older but still common.

</div>
<div class="two">

```python
# 1. Define name variable

name = "Alice"

# 2. Define age variable

age = 30

# 3. f-string

print(f"My name is {name} and I am {age} years old.")

# 4. format()

print("My name is {} and I am {} years old.".format(name, age))
```

</div>
</div>

---

<div class="columns">
<div class="two">

### `input()` function: Getting User Input

- **Purpose:** Get input from the user via the console.
- **Syntax:** `variable = input("Prompt message: ")`
- **Return Type:** Always returns a string.

</div>
<div class="two">

```python
# 1. Ask use for name

user_name = input("Enter your name: ")

# 2. Print personalized greeting

print(f"Hello, {user_name}!")
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Input Type Conversion

- Since `input()` returns a string, you often need to convert it.
- Use `int()`, `float()`, etc., for numerical input.
- **Error Handling:** Be aware of `ValueError` if conversion fails.

</div>
<div class="two">

```python
# 1. Ask use for age

age_str = input("Enter your age: ")

# 2. Convert string to integer

age_int = int(age_str)

# 3. Add 1 to age and print result

print(f"You will be {age_int + 1} next year.")
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Combining Input and Output

- Most interactive programs involve both.
- Prompt the user for information.
- Process the information.
- Display the result.

</div>
<div class="two">

```python
# 1. Ask user for first number

num1 = float(input("Enter first number: "))

# 2. Ask user for second number

num2 = float(input("Enter second number: "))

# 3. Calculate sum

sum_result = num1 + num2

# 4. Print result

print(f"The sum is: {sum_result}")
```

</div>
</div>

---

<div class="columns">
<div class="two">

### Example: Simple Interactive Program

- **Task:** Ask for user's name and favorite color, then greet them.
- **Steps:**
    1.  Get name.
    2.  Get color.
    3.  Print personalized greeting.

</div>
<div class="two">

```python
# 1. Ask user for name

name = input("What is your name? ")

# 2. Ask user for color

color = input("What is your favorite color? ")

# 3. Print name and color

print(f"Hello, {name}! Your favorite color is {color}.")
```

</div>
</div>

---

### Practice Exercise

<div class="columns">
<div class="two">

- **Task:** Create a program that calculates the area of a rectangle.
- **Requirements:**
    - Ask the user for the length.
    - Ask the user for the width.
    - Calculate the area.
    - Print the result in a user-friendly format.

</div>
<div class="two">

```python
# Your code here!
# Hint: Area = length * width
```

</div>
</div>
