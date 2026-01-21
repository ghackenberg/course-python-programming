import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.1, 8.2, 9.8]

# Create Scatter Plot
plt.scatter(x, y, marker='o', color='red', label="Data Points")

# Add Metadata
plt.title("Sensor Calibration")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.grid(True)

# Show Plot
print("Displaying scatter plot...")
plt.show()
