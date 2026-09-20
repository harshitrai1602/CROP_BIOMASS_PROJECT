import pandas as pd
import numpy as np

df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

nir = df["near_infrared"].to_numpy()
red_edge = df["redEdge"].to_numpy()

ndre_calculated = (nir - red_edge) / (nir + red_edge)
ndre_dataset = df["ndre"].to_numpy()

difference = np.abs(ndre_calculated - ndre_dataset)

print("Total observations:", len(df))

print("\nDifference statistics:")
print("Mean difference:", np.mean(difference))
print("Median difference:", np.median(difference))
print("Maximum difference:", np.max(difference))

print("\nRows with difference > 0.01:")
print(np.sum(difference > 0.01))

print("\nRows with difference > 0.05:")
print(np.sum(difference > 0.05))

print("\nRows with difference > 0.10:")
print(np.sum(difference > 0.10))

print("\nRows where Red Edge = 195:")
print(np.sum(df["redEdge"] == 195))
