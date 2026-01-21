import numpy as np

# --- 1D Indexing and Slicing ---
arr = np.array([10, 20, 30, 40, 50])

print(f"Original Array: {arr}")
print(f"Index 0: {arr[0]}")
print(f"Index -1: {arr[-1]}")
print(f"Slice 1:4: {arr[1:4]}")

arr[0:2] = 99
print(f"Modified Array (0:2 = 99): {arr}")

# --- 2D Indexing and Slicing ---
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"\nOriginal Matrix:\n{matrix}")

print(f"\nFirst two rows ([:2, :]):\n{matrix[:2, :]}")

print(f"\nColumn 1 ([:, 1]): {matrix[:, 1]}")

print(f"\nElement at [1, 1]: {matrix[1, 1]}")
