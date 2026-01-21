import numpy as np

# --- Creating Arrays ---
data = [1, 2, 3, 4, 5]
arr = np.array(data)
print(f"Array from list: {arr}")
print(f"Type: {type(arr)}")

# --- Generating Data ---
z = np.zeros(5)
print(f"\nZeros: {z}")

o = np.ones((3, 3))
print(f"\nOnes (3x3):\n{o}")

r = np.arange(0, 10, 2)
print(f"\nRange (0 to 10 step 2): {r}")

l = np.linspace(0, 1, 5)
print(f"\nLinspace (0 to 1 with 5 points): {l}")

# --- Attributes ---
print(f"\nDimensions: {o.ndim}")
print(f"Shape: {o.shape}")
print(f"Size: {o.size}")

# --- Element-wise Operations ---
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(f"\na + b: {a + b}")
print(f"a * b: {a * b}")
print(f"a * 10: {a * 10}")

# --- Broadcasting ---
matrix = np.ones((3, 3))
row = np.array([1, 2, 3])
print(f"\nBroadcasting (Matrix + Row):\n{matrix + row}")
