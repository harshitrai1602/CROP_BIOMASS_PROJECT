import pandas as pd

# -----------------------------
# Ground-truth data
# -----------------------------
gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

# -----------------------------
# March spectral data
# -----------------------------
spectral = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

print("\nGROUND-TRUTH FIRST 10 ROWS")
print("=" * 70)

print(
    gt[
        [
            "Unnamed: 0",
            "BioSense mark",
            "repl.",
            "\nYield(gm)",
            "\nPlant Height(cm)"
        ]
    ].head(10).to_string(index=False)
)


print("\n\nSPECTRAL FIRST 10 ROWS")
print("=" * 70)

print(
    spectral.iloc[:, :10].head(10).to_string(index=False)
)