import pandas as pd
import numpy as np

df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Calculate NDRE
nir = df["near_infrared"].to_numpy()
red_edge = df["redEdge"].to_numpy()

ndre_calculated = (nir - red_edge) / (nir + red_edge)

# Dataset NDRE
ndre_dataset = df["ndre"].to_numpy()

# Absolute difference
difference = np.abs(ndre_calculated - ndre_dataset)

# Add values to dataframe
df["NDRE_calculated"] = ndre_calculated
df["NDRE_difference"] = difference

# Sort by largest difference
problem_rows = df.sort_values(
    "NDRE_difference",
    ascending=False
)

# Display the 10 largest differences
columns = [
    "genotype",
    "near_infrared",
    "redEdge",
    "ndre",
    "NDRE_calculated",
    "NDRE_difference"
]

print("\nLargest NDRE differences:\n")
print(problem_rows[columns].head(10).to_string(index=False))