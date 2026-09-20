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
mean_ndre = []

for date, file_path in files.items():

    df = pd.read_excel(
        file_path,
        sheet_name="Normal"
    )

    # Convert spectral bands to numeric values
    nir = pd.to_numeric(
        df["near_infrared"],
        errors="coerce"
    ).to_numpy()

    red_edge = pd.to_numeric(
        df["redEdge"],
        errors="coerce"
    ).to_numpy()

    # Calculate NDRE
    denominator = nir + red_edge

    ndre = np.divide(
        nir - red_edge,
        denominator,
        out=np.full_like(nir, np.nan, dtype=float),
        where=denominator != 0
    )

    # Ignore missing observations
    average_ndre = np.nanmean(ndre)

    dates.append(date)
    mean_ndre.append(average_ndre)

    print(f"{date}: {average_ndre:.4f}")

# Create graph
plt.figure(figsize=(9, 5))

plt.plot(
    dates,
    mean_ndre,
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Mean NDRE")
plt.title("Mean NDRE Across Crop Growth Dates")

plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig(
    "ndre_growth_stage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
