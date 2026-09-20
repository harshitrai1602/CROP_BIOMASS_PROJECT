import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Original spectral bands
nir = df["near_infrared"].to_numpy()
red = df["red"].to_numpy()

# Calculate NDVI using NumPy
ndvi_calculated = (nir - red) / (nir + red)

# Dataset-provided lowercase NDVI
ndvi_dataset = df["ndvi"].to_numpy()

# Difference
difference = np.abs(ndvi_calculated - ndvi_dataset)

print("First 10 calculated NDVI:")
print(ndvi_calculated[:10])

print("\nFirst 10 dataset NDVI:")
print(ndvi_dataset[:10])

print("\nMaximum absolute difference:")
print(np.max(difference))

print("\nMean absolute difference:")
print(np.mean(difference))