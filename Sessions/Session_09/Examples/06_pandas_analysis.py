import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# --- Selecting Columns ---
ages = df["Age"]
print(f"Average Age: {ages.mean()}")

# --- Selecting Rows (loc/iloc) ---
print(f"\nRow at index 0 (iloc):\n{df.iloc[0]}")

# --- Filtering Data ---
london_residents = df[ df["City"] == "London" ]
print("\nPeople in London:")
print(london_residents)

# Complex filter
high_earners = df[ df["Salary"] > 60000 ]
print("\nHigh Earners (> 60k):")
print(high_earners)

# --- Sorting ---
sorted_df = df.sort_values(by="Age", ascending=False)
print("\nSorted by Age (Descending):")
print(sorted_df)

# --- Engineering Example (Sensor Logs Simulation) ---
# Create a dummy sensor dataframe
sensor_data = pd.DataFrame({
    "Time": [1, 2, 3, 4, 5],
    "Temp": [98, 99, 102, 101, 97]
})

overheating = sensor_data[ sensor_data["Temp"] > 100 ]
print("\nOverheating Sensor Readings:")
print(overheating)
