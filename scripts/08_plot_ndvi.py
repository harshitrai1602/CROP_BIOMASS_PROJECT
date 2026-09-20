import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = {
    "18 Mar 2022": "data/18.03.2022..xlsx",
    "11 Apr 2022": "data/11.04.2022..xlsx",
    "16 May 2022": "data/16.05.2022..xlsx",
    "27 May 2022": "data/27.05.2022..xlsx"
}

dates = []
mean_ndvi = []

for date, file_path in files.items():

    df = pd.read_excel(
        file_path,
        sheet_name="Normal"
    )

    # Convert spectral columns to numeric
    nir = pd.to_numeric(
        df["near_infrared"],
        errors="coerce"
    ).to_numpy()

    red = pd.to_numeric(
        df["red"],
        errors="coerce"
    ).to_numpy()

    # Calculate NDVI
    denominator = nir + red

    ndvi = np.divide(
        nir - red,
        denominator,
        out=np.full_like(nir, np.nan, dtype=float),
        where=denominator != 0
    )

    # Calculate mean while ignoring missing values
    average_ndvi = np.nanmean(ndvi)

    dates.append(date)
    mean_ndvi.append(average_ndvi)

    print(f"{date}: {average_ndvi:.4f}")

# Plot
plt.figure(figsize=(9, 5))

plt.plot(
    dates,
    mean_ndvi,
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Mean NDVI")
plt.title("Mean NDVI Across Crop Growth Dates")

plt.grid(True)
plt.tight_layout()
plt.savefig(
    "ndvi_growth_stage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()