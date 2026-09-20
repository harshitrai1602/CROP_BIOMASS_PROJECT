import pandas as pd

# Load ground truth
gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

# Load spectral data
spectral = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Rename identifiers so their purpose is clear
gt = gt.rename(
    columns={
        "BioSense mark": "id",
        "Unnamed: 2": "gt_genotype",
        "\nYield(gm)": "yield_g",
        "\nPlant Height(cm)": "plant_height_cm"
    }
)

spectral = spectral.rename(
    columns={
        "Unnamed: 0": "id",
        "genotype": "spectral_genotype"
    }
)

# Remove the unmatched / suspicious ground-truth ID
gt_valid = gt[gt["id"] != 1139].copy()

# Merge using the proposed common identifier
merged = pd.merge(
    spectral,
    gt_valid[
        [
            "id",
            "gt_genotype",
            "yield_g",
            "plant_height_cm"
        ]
    ],
    on="id",
    how="inner"
)

print("\nMERGE RESULT")
print("=" * 70)

print("Spectral observations :", len(spectral))
print("Ground-truth valid    :", len(gt_valid))
print("Merged observations   :", len(merged))

print("\nFirst 20 merged records:")
print(
    merged[
        [
            "id",
            "spectral_genotype",
            "gt_genotype",
            "yield_g",
            "plant_height_cm"
        ]
    ]
    .head(20)
    .to_string(index=False)
)

print("\nMissing values in merged ground-truth variables:")
print(
    merged[
        [
            "yield_g",
            "plant_height_cm"
        ]
    ].isna().sum()
)