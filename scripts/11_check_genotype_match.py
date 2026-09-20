import pandas as pd

# -----------------------------
# Ground truth
# -----------------------------
gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

# Ground-truth genotype is stored in Unnamed: 2
gt_genotypes = (
    gt["Unnamed: 2"]
    .astype(str)
    .str.strip()
)

# -----------------------------
# March spectral data
# -----------------------------
spectral = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

spectral_genotypes = (
    spectral["genotype"]
    .astype(str)
    .str.strip()
)

# -----------------------------
# Compare
# -----------------------------
matches = spectral_genotypes.isin(
    gt_genotypes
)

print("\nTotal spectral observations:", len(spectral))

print(
    "Matching genotype observations:",
    matches.sum()
)

print(
    "Non-matching observations:",
    (~matches).sum()
)

print("\nNon-matching spectral genotypes:")

print(
    spectral.loc[
        ~matches,
        "genotype"
    ].value_counts()
)

print("\nFirst 20 spectral genotypes:")
print(spectral_genotypes.head(20).to_string(index=False))