import matplotlib.pyplot as plt

# Data
categories = ["A", "B", "C"]
values = [10, 24, 36]

# Create Bar Chart
plt.bar(categories, values, color="green")

# Add Metadata
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Show Plot
print("Displaying bar chart...")
plt.show()
