import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Extract NIR and Red
nir = df["near_infrared"]
red = df["red"]

# Calculate NDVI using NumPy
ndvi_calculated = (nir - red) / (nir + red)

# Add our calculated NDVI to the dataframe
df["NDVI_calculated"] = ndvi_calculated

# Display comparison
print("\nNDVI comparison:\n")

print(
    df[
        ["near_infrared", "red", "NDVI", "NDVI_calculated"]
    ].head(10)
)
