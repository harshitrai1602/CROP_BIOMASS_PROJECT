import pandas as pd

gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

spectral = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Convert identifiers to numeric
gt_mark = pd.to_numeric(
    gt["BioSense mark"],
    errors="coerce"
)

spectral_id = pd.to_numeric(
    spectral["Unnamed: 0"],
    errors="coerce"
)

# Compare the two identifier sets
gt_ids = set(gt_mark.dropna())
spectral_ids = set(spectral_id.dropna())

common_ids = gt_ids.intersection(spectral_ids)

print("\nIDENTIFIER MAPPING TEST")
print("=" * 70)

print("Ground-truth IDs       :", len(gt_ids))
print("Spectral IDs            :", len(spectral_ids))
print("Common IDs              :", len(common_ids))

print("\nGround-truth IDs not in spectral:")
print(sorted(gt_ids - spectral_ids))

print("\nSpectral IDs not in ground-truth:")
print(sorted(spectral_ids - gt_ids))

# Create a mapping using:
# GT BioSense mark -> Spectral Unnamed: 0
mapping = pd.DataFrame({
    "BioSense_mark": sorted(common_ids)
})

mapping["spectral_Unnamed_0"] = mapping["BioSense_mark"]

print("\nFirst 20 proposed mappings:")
print(mapping.head(20).to_string(index=False))