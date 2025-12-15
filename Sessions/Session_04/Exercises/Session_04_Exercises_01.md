# Exercises 04: Modules, Packages & File I/O

Welcome to the exercises for Session 04! This sheet will help you practice organizing code with modules and handling data with file I/O operations.

## 4.1: Importing Modules

1.  **Vector Magnitude:** Import the `math` module. Write a script that calculates the magnitude of a 2D vector with components `x = 3` and `y = 4`. The formula is $\text{magnitude} = \sqrt{x^2 + y^2}$. Use `math.sqrt()` and `math.pow()` or the `**` operator.

2.  **Process Logging:** Import the `datetime` module. Write a script that prints the current time in the format `YYYY-MM-DD HH:MM:SS` and then prints "Process complete." Use `datetime.now()` and `.strftime()`.

3.  **Simulation Input:** Import the `random` module and give it an alias `rnd`. Write a script that generates a random integer between 900 and 1100 to simulate a "motor_rpm" reading and prints it. Use `rnd.randint()`.

## 4.2: Creating Custom Modules

1.  **Unit Conversions Module:**
    -   Create a Python file named `conversions.py`.
    -   Inside this module, define a function `inches_to_mm(inches)` that takes a value in inches and returns the equivalent in millimeters (1 inch = 25.4 mm).
    -   Create a second file named `main.py`. In this file, import your `conversions` module and use it to convert 10 inches to millimeters, then print the result.

2.  **Test Block:**
    -   Go back to your `conversions.py` file.
    -   Add an `if __name__ == "__main__":` block at the end.
    -   Inside this block, add a print statement like "Running module tests..." and then test your `inches_to_mm` function with a few values (e.g., 1, 10, 0.5), printing the results to verify it works correctly.
    -   Run `python conversions.py` directly to see your test output. Then run `python main.py` to ensure the test block doesn't execute when the module is imported.

## 4.3: Reading from Files

1.  **Read a Report:** Create a text file named `report.txt` and write a few lines of text into it (e.g., "Analysis complete.", "All systems nominal."). Write a Python script that opens `report.txt`, reads its entire content, and prints it to the console. Use the `with open(...)` syntax.

2.  **Parse Configuration:** Create a file `settings.txt` with the following content:
    ```
    device_id=TEMP-001
    port=COM3
    baud_rate=9600
    ```
    Write a script that reads this file line by line. For each line, split it at the `=` character to separate the key and value, and store them in a dictionary. Finally, print the dictionary.

3.  **Load JSON Data:** Create a file `part_spec.json` with the following content:
    ```json
    {
      "part_id": "PN-54321",
      "material": "Aluminum 6061",
      "dimensions": {
        "width": 50,
        "height": 100,
        "unit": "mm"
      }
    }
    ```
    Write a Python script using the `json` module to load this file into a dictionary. Then, print the `material` and the `width` of the part.

## 4.4: Writing to Files

1.  **Save Results:** Write a script that calculates the result of a simple formula (e.g., `area = 15.5 * 20.3`). The script should then create a file named `result.txt` and write the result in a human-readable sentence, like "The calculated area is 314.65 square meters."

2.  **Error Logging:** Create a function `log_error(error_code, message)`. This function should append a formatted error message, including the current timestamp, to a file named `errors.log`. Example line: `[2025-12-15 14:45:01] - ERROR 404: File not found.` Call this function two or three times with different messages.

3.  **Generate a CSV File:** You have a list of sensor data measurements as a list of lists:
    ```python
    data = [
        ["Time", "Temperature", "Pressure"],
        ["10:01", "22.5", "101.3"],
        ["10:02", "22.6", "101.2"],
        ["10:03", "22.7", "101.3"]
    ]
    ```
    Write a script using the `csv` module to write this data into a new file called `sensor_output.csv`. The first inner list should be the header.
