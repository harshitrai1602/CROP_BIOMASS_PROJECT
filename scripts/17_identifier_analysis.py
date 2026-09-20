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

print("\nGROUND TRUTH IDENTIFIERS")
print("=" * 70)

print("BioSense mark:")
print(
    gt["BioSense mark"]
    .dropna()
    .tolist()
)

print("\nGround truth Unnamed: 0:")
print(
    gt["Unnamed: 0"]
    .dropna()
    .tolist()
)

print("\n\nSPECTRAL IDENTIFIERS")
print("=" * 70)

print("Spectral Unnamed: 0:")
print(
    spectral["Unnamed: 0"]
    .dropna()
    .tolist()
)

print("\nSpectral code:")
print(
    spectral["code"]
    .dropna()
    .tolist()
)