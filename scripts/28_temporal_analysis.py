import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load clean dataset
# --------------------------------------------------

file_path = "data/crop_biomass_analysis.csv"

df = pd.read_csv(file_path)


# --------------------------------------------------
# Define date order
# --------------------------------------------------

date_order = [
    "18 Mar 2022",
    "11 Apr 2022",
    "16 May 2022",
    "27 May 2022"
]

df["date"] = pd.Categorical(
    df["date"],
    categories=date_order,
    ordered=True
)


# --------------------------------------------------
# Calculate mean vegetation indices
# --------------------------------------------------

summary = (
    df.groupby(
        "date",
        observed=True
    )[
        [
            "NDVI_calculated",
            "NDRE_calculated",
            "EVI"
        ]
    ]
    .mean()
    .reindex(date_order)
)


print("\nTEMPORAL VEGETATION INDEX SUMMARY")
print("=" * 70)

print(
    summary.to_string()
)


# --------------------------------------------------
# Print valid observation counts
# --------------------------------------------------

print("\n\nVALID OBSERVATIONS")
print("=" * 70)

valid_counts = (
    df.groupby(
        "date",
        observed=True
    )[
        [
            "NDVI_calculated",
            "NDRE_calculated",
            "EVI"
        ]
    ]
    .count()
    .reindex(date_order)
)

print(
    valid_counts.to_string()
)


# --------------------------------------------------
# Plot NDVI
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    summary.index,
    summary["NDVI_calculated"],
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Mean NDVI")

plt.title(
    "Mean NDVI Across Crop Growth Dates"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "data/ndvi_temporal_analysis.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# Plot NDRE
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    summary.index,
    summary["NDRE_calculated"],
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Mean NDRE")

plt.title(
    "Mean NDRE Across Crop Growth Dates"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "data/ndre_temporal_analysis.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# Plot EVI
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    summary.index,
    summary["EVI"],
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Mean EVI")

plt.title(
    "Mean EVI Across Crop Growth Dates"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "data/evi_temporal_analysis.png",
    dpi=300
)

plt.show()