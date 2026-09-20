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

print("\nGROUND TRUTH RECORD WITH BioSense mark = 1139")
print("=" * 70)

print(
    gt[gt["BioSense mark"] == 1139].to_string(index=False)
)

print("\n\nGROUND TRUTH RECORD WITH BioSense mark = 113")
print("=" * 70)

print(
    gt[gt["BioSense mark"] == 113].to_string(index=False)
)

print("\n\nSPECTRAL RECORD WITH Unnamed: 0 = 113")
print("=" * 70)

print(
    spectral[spectral["Unnamed: 0"] == 113].to_string(index=False)
)