import pandas as pd

# Dataset file
file_path = "data/18.03.2022..xlsx"

# Read the Normal sheet
df = pd.read_excel(file_path, sheet_name="Normal")

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Show dataset dimensions
print("\nDataset shape:")
print(df.shape)

# Show column names
print("\nColumn names:")
print(df.columns.tolist())