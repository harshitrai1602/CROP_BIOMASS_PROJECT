import pandas as pd
import numpy as np

files = {
    "18 Mar 2022": "data/18.03.2022..xlsx",
    "11 Apr 2022": "data/11.04.2022..xlsx",
    "16 May 2022": "data/16.05.2022..xlsx",
    "27 May 2022": "data/27.05.2022..xlsx"
}

# --------------------------------------------------
# Ground truth
# --------------------------------------------------

gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

gt = gt.rename(
    columns={
        "BioSense mark": "id",
        "\nYield(gm)": "yield_g",
        "\nPlant Height(cm)": "plant_height_cm"
    }
)

# Remove the unmatched ground-truth observation
gt = gt[gt["id"] != 1139].copy()

# --------------------------------------------------
# Date-wise analysis
# --------------------------------------------------

print("\nDATE-WISE CORRELATION")
print("=" * 90)

for date, file_path in files.items():

    spectral = pd.read_excel(
        file_path,
        sheet_name="Normal"
    )

    # --------------------------------------------------
    # Identify the observation ID column
    # --------------------------------------------------

    if "Unnamed: 0" in spectral.columns:
        spectral = spectral.rename(
            columns={"Unnamed: 0": "id"}
        )

    elif "id" not in spectral.columns:

        # Use the first column as the observation ID
        first_column = spectral.columns[0]

        spectral = spectral.rename(
            columns={first_column: "id"}
        )

    # --------------------------------------------------
    # Merge
    # --------------------------------------------------

    merged = pd.merge(
        spectral,
        gt[
            [
                "id",
                "yield_g",
                "plant_height_cm"
            ]
        ],
        on="id",
        how="inner"
    )

    # --------------------------------------------------
    # Convert spectral bands
    # --------------------------------------------------

    nir = pd.to_numeric(
        merged["near_infrared"],
        errors="coerce"
    ).to_numpy(dtype=float)

    red = pd.to_numeric(
        merged["red"],
        errors="coerce"
    ).to_numpy(dtype=float)

    red_edge = pd.to_numeric(
        merged["redEdge"],
        errors="coerce"
    ).to_numpy(dtype=float)

    # --------------------------------------------------
    # NDVI
    # --------------------------------------------------

    ndvi_denominator = nir + red

    merged["NDVI"] = np.divide(
        nir - red,
        ndvi_denominator,
        out=np.full_like(nir, np.nan),
        where=ndvi_denominator != 0
    )

    # --------------------------------------------------
    # NDRE
    # --------------------------------------------------

    ndre_denominator = nir + red_edge

    merged["NDRE"] = np.divide(
        nir - red_edge,
        ndre_denominator,
        out=np.full_like(nir, np.nan),
        where=ndre_denominator != 0
    )

    # --------------------------------------------------
    # Dataset-provided EVI
    # --------------------------------------------------

    merged["EVI_analysis"] = pd.to_numeric(
        merged["EVI"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    print(f"\n{date}")
    print("-" * 70)

    for feature in ["NDVI", "NDRE", "EVI_analysis"]:

        valid = merged[
            [feature, "yield_g"]
        ].dropna()

        r = valid[feature].corr(
            valid["yield_g"]
        )

        print(
            f"{feature:12} vs Yield: "
            f"r = {r:.4f} "
            f"(n = {len(valid)})"
        )