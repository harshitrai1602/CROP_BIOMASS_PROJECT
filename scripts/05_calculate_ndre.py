import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Extract spectral bands
nir = df["near_infrared"].to_numpy()
red_edge = df["redEdge"].to_numpy()

# Calculate NDRE
ndre_calculated = (nir - red_edge) / (nir + red_edge)

# Dataset-provided NDRE
ndre_dataset = df["ndre"].to_numpy()

# Calculate absolute difference
difference = np.abs(ndre_calculated - ndre_dataset)

print("\nFirst 10 NDRE values:\n")

print("Calculated NDRE:")
print(ndre_calculated[:10])

print("\nDataset NDRE:")
print(ndre_dataset[:10])

print("\nMaximum absolute difference:")
print(np.max(difference))

print("\nMean absolute difference:")
print(np.mean(difference))
