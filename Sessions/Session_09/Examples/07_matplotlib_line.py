import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create Plot
plt.plot(x, y, color="blue", linestyle="--", linewidth=2, label="Sine Wave")

# Add Metadata
plt.title("Simple Harmonic Motion")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (m)")

# Add Legend and Grid
plt.legend()
plt.grid(True)

# Show Plot
print("Displaying plot...")
plt.show()
