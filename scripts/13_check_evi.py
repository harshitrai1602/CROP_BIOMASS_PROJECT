import pandas as pd

df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

columns = [
    "near_infrared",
    "red",
    "blue",
    "EVI"
]

print("\nEVI-related data:\n")
print(
    df[columns]
    .head(10)
    .to_string(index=False)
)

print("\nMissing values:")
print(df[columns].isna().sum())
