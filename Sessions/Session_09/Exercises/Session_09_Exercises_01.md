# Exercises 09: Working with External Libraries

Welcome to the exercises for Session 09! This sheet will help you practice using the most important external libraries in the Python ecosystem: NumPy, Pandas, and Matplotlib.

## 9.1: Installing Packages with pip

1.  **Definitions:** Briefly explain the difference between a *Module*, a *Package*, and a *Library* in Python.
2.  **Using pip:** Provide the terminal commands to:
    -   Install the library `pandas` with exactly version `1.3.0`.
    -   Upgrade an existing `numpy` installation to the latest version.
    -   List all currently installed packages in your environment.
3.  **Dependency Management:**
    -   What is the purpose of a `requirements.txt` file?
    -   How can you automatically generate this file from your current environment?
    -   What command would another developer use to install all dependencies from your `requirements.txt`?

## 9.2: Introduction to NumPy

1.  **Lists vs. Arrays:** Name two reasons why NumPy arrays are preferred over standard Python lists for numerical computations.
2.  **Array Creation:** Write the NumPy code to create the following:
    -   A 1D array of 10 zeros.
    -   A 3x3 matrix filled with ones.
    -   An array with values from 0 to 100 with a step of 5.
    -   An array of 10 evenly spaced points between 0 and 1.
3.  **Attributes:** You have an array `A = np.zeros((4, 5, 6))`. What will be the output of `A.ndim`, `A.shape`, and `A.size`?
4.  **Vectorization:** Given `x = np.array([1, 2, 3])`, write the code to create `y` where every element of `x` is multiplied by 10 and then squared. (Do not use loops!)

## 9.3: Introduction to Pandas

1.  **Data Structures:** Explain the relationship between a Pandas `Series` and a `DataFrame`.
2.  **Data Inspection:** You have just loaded a large CSV file into a DataFrame named `df`. Which commands would you use to:
    -   See the first 10 rows.
    -   Get a summary of data types and missing values.
    -   Get statistical summaries (mean, std, min, max) of numerical columns.
3.  **Selection & Filtering:**
    -   Select a single column named "Temperature".
    -   Select the first 5 rows using integer-based indexing (`iloc`).
    -   Filter the DataFrame to show only rows where "Pressure" is greater than 100.
4.  **Calculations:** How would you create a new column "Efficiency" by dividing the "Output" column by the "Input" column?

## 9.4: Introduction to Matplotlib

1.  **Basic Plotting:** Write a script that plots a simple line graph of `y = x**3` for `x` values from -5 to 5.
2.  **Customization:** List the commands to add a title, x-axis label, y-axis label, and a grid to your plot.
3.  **Plot Types:** When would you choose a `scatter` plot over a `line` plot? When is a `histogram` most useful?
4.  **Subplots:** Explain the meaning of the arguments in `plt.subplot(2, 1, 1)`.
5.  **Saving:** Write the code to save your current plot as a high-resolution PNG file named `my_results.png`.
