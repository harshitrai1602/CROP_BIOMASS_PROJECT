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
ndvi_means = []
ndre_means = []
evi_means = []

for date, file_path in files.items():

    df = pd.read_excel(file_path, sheet_name="Normal")

    nir = pd.to_numeric(
        df["near_infrared"], errors="coerce"
    ).to_numpy()

    red = pd.to_numeric(
        df["red"], errors="coerce"
    ).to_numpy()

    red_edge = pd.to_numeric(
        df["redEdge"], errors="coerce"
    ).to_numpy()

    evi = pd.to_numeric(
        df["EVI"], errors="coerce"
    ).to_numpy()

    # NDVI
    ndvi_denominator = nir + red

    ndvi = np.divide(
        nir - red,
        ndvi_denominator,
        out=np.full_like(nir, np.nan),
        where=ndvi_denominator != 0
    )

    # NDRE
    ndre_denominator = nir + red_edge

    ndre = np.divide(
        nir - red_edge,
        ndre_denominator,
        out=np.full_like(nir, np.nan),
        where=ndre_denominator != 0
    )

    dates.append(date)
    ndvi_means.append(np.nanmean(ndvi))
    ndre_means.append(np.nanmean(ndre))
    evi_means.append(np.nanmean(evi))


print("\nMean vegetation indices:")
print("=" * 60)

for i in range(len(dates)):
    print(
        f"{dates[i]:12} | "
        f"NDVI: {ndvi_means[i]:.4f} | "
        f"NDRE: {ndre_means[i]:.4f} | "
        f"EVI: {evi_means[i]:.4f}"
    )


# Plot
x = np.arange(len(dates))

plt.figure(figsize=(10, 6))

plt.plot(x, ndvi_means, marker="o", label="NDVI")
plt.plot(x, ndre_means, marker="o", label="NDRE")
plt.plot(x, evi_means, marker="o", label="EVI")

plt.xticks(x, dates)
plt.xlabel("Observation Date")
plt.ylabel("Mean Index Value")
plt.title("Vegetation Index Variation Across Observation Dates")

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    "ndvi_ndre_evi_comparison.png",
    dpi=300
)

plt.show()
