# Exercises 03: Data Structures II & Functions

Welcome to the exercises for Session 03! This sheet will help you practice using dictionaries, sets, and creating your own functions.

## 3.1: Dictionaries

1.  **Inventory Management:** Create a dictionary `inventory` to represent stock.
    -   Initialize it with `"screws": 500`, `"nuts": 800`, and `"bolts": 1200`.
    -   Add a new item: `"washers": 1000`.
    -   Update the quantity of `"nuts"` to 850.
    -   Remove `"bolts"` from the inventory.
    -   Print the final inventory.

2.  **Machine Configuration:** Create a dictionary to store a machine's configuration settings: `machine_config = {"name": "CNC Mill", "speed": 1200, "axis": 3}`.
    -   Write code to safely access the `"tool_type"` using `.get()`. If it doesn't exist, it should return `"default"`. Print the result.
    -   Iterate through the dictionary and print each setting as `Key -> Value`.

3.  **Error Code Lookup:** Create a dictionary `error_codes` mapping codes to messages: `{100: "Connection Error", 205: "Timeout", 404: "Resource Not Found"}`.
    -   Write code that checks if the code `205` exists in the dictionary and prints its message.
    -   Check if code `500` exists. If not, print "Unknown Error Code".

## 3.2: Sets

1.  **Removing Duplicates:** You have a list of part serial numbers with some duplicates: `serial_numbers = ["SN001", "SN002", "SN001", "SN003", "SN004", "SN002"]`.
    -   Use a set to find all the *unique* serial numbers.
    -   Convert the set back to a list and print it.

2.  **Skill Matching:** A job requires a set of skills: `required_skills = {"Python", "SQL", "Git"}`. An applicant has the following skills: `applicant_skills = {"Python", "Java", "Git", "C++"}`.
    -   Find the skills that are common to both sets (intersection).
    -   Find the required skills that the applicant is missing (difference).
    -   Find all skills from both sets combined (union).

3.  **User Access Control:** You have two sets of user IDs. `admins = {"user1", "user5", "user8"}` and `moderators = {"user2", "user5", "user9"}`.
    -   Create a new set `all_privileged_users` containing all users who are either admins or moderators.
    -   Find the users who are both admins and moderators.
    -   Find the users who are admins but not moderators.

## 3.3: Defining Functions

1.  **Safety Warning:** Write a function `display_safety_warning()` that prints a standard safety message, like "--- WARNING: Ensure all safety guards are in place before operating. ---". Call this function.

2.  **System Startup Check:** Write a function `system_check()` that prints the following messages:
    - "Checking power supply..."
    - "Checking sensor connections..."
    - "System ready."
    - Call this function twice.

3.  **Variable Scope:**
    -   Define a global variable `factory_id = "F-101"`.
    -   Write a function `print_machine_info()` that defines a local variable `machine_id = "M-202"` and prints both `factory_id` and `machine_id`.
    -   Call the function.
    -   After the function call, try to print `machine_id` and observe the `NameError`. (You can comment out the line that causes the error after seeing it).

## 3.4: Function Arguments and Return Values

1.  **Temperature Converter:**
    -   Write a function `celsius_to_fahrenheit(celsius)` that takes a temperature in Celsius, calculates the Fahrenheit value (`F = C * 9/5 + 32`), and **returns** it.
    -   Call the function with `25` as the argument and print the returned result.

2.  **Create Report:**
    -   Write a function `create_report(title, author, level="OFFICIAL")` that has a default argument for `level`.
    -   The function should return a formatted string, like: `f"{title} | By: {author} | Level: {level}"`.
    -   Call the function once with just a title and author.
    -   Call it again, but this time specify the `level` as `"CONFIDENTIAL"`. Print the results of both calls.

3.  **Analyze Sensor Data:**
    -   Write a function `analyze_data(readings)` that takes a list of numbers.
    -   The function should return the minimum, maximum, and average of the readings as a single tuple. (You can use the built-in `min()`, `max()`, and `sum()/len()` functions).
    -   Call the function with `[10.2, 10.5, 9.9, 11.1, 10.8]` and unpack the returned tuple into three separate variables: `min_val`, `max_val`, `avg_val`. Print each variable.
