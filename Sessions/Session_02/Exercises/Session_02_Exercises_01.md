# Exercises 02: Control Flow & Data Structures I

Welcome to the exercises for Session 02! This sheet will help you practice your understanding of conditional statements, loops, lists, and tuples in Python.

## 2.1: Conditional Statements (if/else)

1.  **Safety Interlock:** Write a program that simulates a machine safety door. If the `door_is_closed` and `safety_sensor_active` are both `True`, print "Machine can start". Otherwise, print "SAFETY ALERT: Cannot start machine."

2.  **Quality Control:** A component's length should be between 24.9mm and 25.1mm. Write code that checks a `measured_length` and prints "Pass", "Reject: Too short", or "Reject: Too long".

3.  **Engine Diagnostics:** Write a program that checks `engine_temp` and `oil_pressure`. Print "Shutdown!" if temp is over 110°C or pressure is below 5 PSI. Print "Warning" if temp is over 90°C. Otherwise, print "Normal".

## 2.2: Loops (for/while)

1.  **Countdown:** Write a `while` loop that counts down from 10 to 1 and then prints "Liftoff!".

2.  **Sum of Squares:** Use a `for` loop and `range()` to calculate the sum of the squares of the first 10 integers (1² + 2² + ... + 10²). The formula for the sum is $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$. Check if your code matches the formula's result for n=10.

3.  **Data Filtering:** You have a list of temperature readings: `temps = [35.2, 36.1, 37.5, 40.2, 35.9, 33.4]`. Use a `for` loop to iterate through them. If a temperature is above 38.0, print a "Fever Alert!" and `break` the loop. Use `continue` to skip any temperature below 35.0.

## 2.3: Lists

1.  **Maintenance Log:** Create a list of maintenance tasks `tasks = ["Check Oil", "Calibrate Sensor", "Replace Filter"]`.
    -   Add "Inspect Belts" to the end of the list.
    -   Remove "Calibrate Sensor".
    -   Sort the list alphabetically and print it.

2.  **Signal Processing:** You have a list of noisy signal data: `signal = [1, 5, 2, 8, 3, 9, 4]`. Create a new list called `processed_signal` that contains only the values from `signal` that are greater than 4. (Use a loop and an `if` condition).

3.  **Matrix Trace:** Given a 3x3 matrix (list of lists), write code to calculate its trace (the sum of the elements on the main diagonal: top-left to bottom-right).
    `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> Trace is 1 + 5 + 9 = 15.

## 2.4: Tuples

1.  **Configuration:** Create a tuple to store a motor's configuration: `("DC", 12, 5000)` for (Type, Voltage, Max RPM). Try to change the voltage to 24. What happens?

2.  **Multi-Return Function:** Write a function `calculate_stats(numbers)` that takes a list of numbers and returns a tuple containing the minimum, maximum, and average of those numbers. Test it with a sample list.

3.  **Unpacking:** A function returns a tuple `result = ("Success", 192.168.1.100")`. Unpack this tuple into two variables, `status` and `ip_address`, and print them.
