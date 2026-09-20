import pandas as pd
import numpy as np

# --------------------------------------------------
# Load data
# --------------------------------------------------

gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

spectral = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# --------------------------------------------------
# Prepare ground truth
# --------------------------------------------------

gt = gt.rename(
    columns={
        "BioSense mark": "id",
        "\nYield(gm)": "yield_g",
        "\nPlant Height(cm)": "plant_height_cm"
    }
)

# Remove the unmatched ground-truth observation
gt = gt[gt["id"] != 1139].copy()

# --------------------------------------------------
# Prepare spectral data
# --------------------------------------------------

spectral = spectral.rename(
    columns={
        "Unnamed: 0": "id"
    }
)

# --------------------------------------------------
# Merge
# --------------------------------------------------

merged = pd.merge(
    spectral,
    gt[
        [
            "id",
            "yield_g",
            "plant_height_cm"
        ]
    ],
    on="id",
    how="inner"
)

# --------------------------------------------------
# Calculate NDVI independently
# --------------------------------------------------

nir = pd.to_numeric(
    merged["near_infrared"],
    errors="coerce"
).to_numpy(dtype=float)

red = pd.to_numeric(
    merged["red"],
    errors="coerce"
).to_numpy(dtype=float)

ndvi_denominator = nir + red

merged["NDVI_calculated"] = np.divide(
    nir - red,
    ndvi_denominator,
    out=np.full_like(nir, np.nan),
    where=ndvi_denominator != 0
)

# --------------------------------------------------
# Calculate NDRE independently
# --------------------------------------------------

red_edge = pd.to_numeric(
    merged["redEdge"],
    errors="coerce"
).to_numpy(dtype=float)

ndre_denominator = nir + red_edge

merged["NDRE_calculated"] = np.divide(
    nir - red_edge,
    ndre_denominator,
    out=np.full_like(nir, np.nan),
    where=ndre_denominator != 0
)

# --------------------------------------------------
# Use dataset-provided EVI
# --------------------------------------------------

merged["EVI_provided"] = pd.to_numeric(
    merged["EVI"],
    errors="coerce"
)

# --------------------------------------------------
# Correlation analysis
# --------------------------------------------------

features = [
    "NDVI_calculated",
    "NDRE_calculated",
    "EVI_provided"
]

targets = [
    "yield_g",
    "plant_height_cm"
]

print("\nCORRELATION ANALYSIS")
print("=" * 70)

for feature in features:

    print(f"\n{feature}")
    print("-" * 50)

    for target in targets:

        valid = merged[
            [feature, target]
        ].dropna()

        correlation = valid[feature].corr(
            valid[target]
        )

        print(
            f"{target:20} r = {correlation:.4f}"
        )

# --------------------------------------------------
# Save merged dataset
# --------------------------------------------------

merged.to_csv(
    "merged_spectral_ground_truth.csv",
    index=False
)

print("\nMerged dataset saved as:")
print("merged_spectral_ground_truth.csv")