import matplotlib.pyplot as plt
import numpy as np

# Generate random data (normal distribution)
data = np.random.randn(1000)

# Create Histogram
plt.hist(data, bins=30, alpha=0.7, color='purple', edgecolor='black')

# Add Metadata
plt.title("Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show Plot
print("Displaying histogram...")
plt.show()
