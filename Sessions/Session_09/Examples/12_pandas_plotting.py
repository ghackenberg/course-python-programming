import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 130, 170, 200],
    "Profit": [20, 45, 30, 60, 80]
})

# Plotting with Pandas
# Line plot of Sales
df.plot(x="Month", y="Sales", kind="line", marker="o")
plt.title("Monthly Sales")
plt.grid(True)

# Scatter plot: Sales vs Profit
df.plot(x="Sales", y="Profit", kind="scatter", color="red")
plt.title("Sales vs Profit Correlation")
plt.grid(True)

# Bar plot of Profit
df.plot(x="Month", y="Profit", kind="bar", color="green")
plt.title("Monthly Profit")

# Show all plots
print("Displaying Pandas plots...")
plt.show()
