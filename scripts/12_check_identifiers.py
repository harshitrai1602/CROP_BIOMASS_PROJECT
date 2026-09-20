import pandas as pd

# Ground truth
gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

# Spectral data
spectral = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

print("\nGROUND TRUTH")
print("=" * 70)

print(
    gt[
        [
            "Unnamed: 0",
            "BioSense mark",
            "\nYield(gm)",
            "\nPlant Height(cm)"
        ]
    ].head(20).to_string(index=False)
)

print("\n\nSPECTRAL DATA")
print("=" * 70)

print(
    spectral[
        [
            "Unnamed: 0",
            "code",
            "genotype"
        ]
    ].head(20).to_string(index=False)
)