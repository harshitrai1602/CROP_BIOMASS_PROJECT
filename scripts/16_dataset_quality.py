import pandas as pd

files = {
    "18 Mar 2022": "data/18.03.2022..xlsx",
    "11 Apr 2022": "data/11.04.2022..xlsx",
    "16 May 2022": "data/16.05.2022..xlsx",
    "27 May 2022": "data/27.05.2022..xlsx"
}

print("\nDATASET QUALITY CHECK")
print("=" * 90)

for date, file_path in files.items():

    df = pd.read_excel(
        file_path,
        sheet_name="Normal"
    )

    total = len(df)

    nir_missing = df["near_infrared"].isna().sum()
    red_missing = df["red"].isna().sum()
    rededge_missing = df["redEdge"].isna().sum()
    evi_missing = df["EVI"].isna().sum()

    valid_nir_red = df[
        df["near_infrared"].notna() &
        df["red"].notna()
    ].shape[0]

    print(f"\n{date}")
    print("-" * 50)
    print("Total observations :", total)
    print("Missing NIR        :", nir_missing)
    print("Missing Red        :", red_missing)
    print("Missing Red Edge   :", rededge_missing)
    print("Missing EVI        :", evi_missing)
    print("Valid NIR + Red    :", valid_nir_red)