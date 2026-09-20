import pandas as pd
import numpy as np

df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Extract spectral bands
nir = df["near_infrared"].to_numpy(dtype=float)
red = df["red"].to_numpy(dtype=float)
blue = df["blue"].to_numpy(dtype=float)

# Standard EVI formula
evi_calculated = 2.5 * (
    (nir - red) /
    (nir + 6 * red - 7.5 * blue + 1)
)

# Dataset-provided EVI
evi_dataset = df["EVI"].to_numpy(dtype=float)

# Absolute difference
difference = np.abs(evi_calculated - evi_dataset)

print("\nFirst 10 calculated EVI values:")
print(evi_calculated[:10])

print("\nFirst 10 dataset EVI values:")
print(evi_dataset[:10])

print("\nFirst 10 absolute differences:")
print(difference[:10])

print("\nValidation:")
print("Mean absolute difference:", np.mean(difference))
print("Median absolute difference:", np.median(difference))
print("Maximum absolute difference:", np.max(difference))
