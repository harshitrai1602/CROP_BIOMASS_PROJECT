import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load dataset
# --------------------------------------------------

df = pd.read_csv(
    "data/crop_biomass_analysis.csv"
)


# --------------------------------------------------
# Date order
# --------------------------------------------------

date_order = [
    "18 Mar 2022",
    "11 Apr 2022",
    "16 May 2022",
    "27 May 2022"
]


# --------------------------------------------------
# Index information
# --------------------------------------------------

indices = {
    "NDVI_calculated": "NDVI",
    "NDRE_calculated": "NDRE",
    "EVI": "EVI"
}


# --------------------------------------------------
# Create one figure per index
# --------------------------------------------------

for column, label in indices.items():

    plt.figure(figsize=(8, 6))

    for date in date_order:

        subset = df[
            df["date"] == date
        ][
            [column, "yield_g"]
        ].dropna()

        plt.scatter(
            subset[column],
            subset["yield_g"],
            label=date,
            alpha=0.7
        )

    plt.xlabel(label)
    plt.ylabel("Yield (g)")

    plt.title(
        f"{label} vs Ground-Truth Yield"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    filename = (
        f"data/{label.lower()}_vs_yield.png"
    )

    plt.savefig(
        filename,
        dpi=300
    )

    plt.show()

    print(
        f"Saved: {filename}"
    )