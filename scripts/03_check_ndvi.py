import pandas as pd

df = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Show the important spectral/index columns
columns = [
    "near_infrared",
    "red",
    "redEdge",
    "infrared",
    "NDVI",
    "ndvi",
    "near_infrared.1",
    "red.1",
    "redEdge.1",
    "NDVI.1"
]

print(df[columns].head(10).to_string(index=False))