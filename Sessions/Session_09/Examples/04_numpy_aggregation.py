import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

print(f"Array:\n{arr}")

total = np.sum(arr)
print(f"\nTotal Sum: {total}")

col_sum = np.sum(arr, axis=0)
print(f"Sum of columns (axis=0): {col_sum}")

row_sum = np.sum(arr, axis=1)
print(f"Sum of rows (axis=1): {row_sum}")
