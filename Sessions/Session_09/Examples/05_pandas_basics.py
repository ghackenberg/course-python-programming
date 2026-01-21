import pandas as pd

# --- Series ---
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Pandas Series:")
print(s)
print(f"Value at 'a': {s['a']}")

# --- DataFrame from Dictionary ---
data = {
    "Name": ["Alice", "Bob"],
    "Age": [25, 30],
    "City": ["London", "Paris"]
}
df_dict = pd.DataFrame(data)
print("\nDataFrame from Dictionary:")
print(df_dict)

# --- Loading Data from CSV ---
print("\nLoading data from 'data.csv'...")
df = pd.read_csv("data.csv")

# --- Inspecting Data ---
print("\nFirst 3 rows (head):")
print(df.head(3))

print("\nData Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())
