import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 5, 50)
y1 = np.exp(x)
y2 = np.log(x + 1)

# Create Subplots (1 row, 2 columns)
plt.figure(figsize=(10, 4))

# Subplot 1: Exponential
plt.subplot(1, 2, 1)
plt.plot(x, y1, color="red")
plt.title("Exponential Growth")
plt.grid(True)

# Subplot 2: Logarithmic
plt.subplot(1, 2, 2)
plt.plot(x, y2, color="blue")
plt.title("Logarithmic Growth")
plt.grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show Plot
print("Displaying subplots...")
plt.show()
