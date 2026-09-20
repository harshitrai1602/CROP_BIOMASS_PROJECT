import pandas as pd
import numpy as np


# --------------------------------------------------
# File paths
# --------------------------------------------------

files = {
    "18 Mar 2022": "data/18.03.2022..xlsx",
    "11 Apr 2022": "data/11.04.2022..xlsx",
    "16 May 2022": "data/16.05.2022..xlsx",
    "27 May 2022": "data/27.05.2022..xlsx"
}


# --------------------------------------------------
# Load ground-truth data
# --------------------------------------------------

gt = pd.read_excel(
    "data/GT_data.xlsx",
    sheet_name="Sheet1",
    header=1
)

gt = gt.rename(columns={
    "Unnamed: 0": "gt_id",
    "BioSense mark": "sample_id",
    "\nYield(gm)": "yield_g",
    "\nPlant Height(cm)": "plant_height_cm"
})

gt = gt[
    [
        "sample_id",
        "yield_g",
        "plant_height_cm"
    ]
].copy()

gt["sample_id"] = pd.to_numeric(
    gt["sample_id"],
    errors="coerce"
)

gt = gt.dropna(subset=["sample_id"])

gt["sample_id"] = gt["sample_id"].astype(int)


# --------------------------------------------------
# Process each date
# --------------------------------------------------

all_data = []

for date, file_path in files.items():

    df = pd.read_excel(
        file_path,
        sheet_name="Normal"
    )

    # Remove completely empty rows
    df = df.dropna(
    subset=["genotype"]
).copy()

    # ----------------------------------------------
    # Identify sample ID
    # ----------------------------------------------

    if date == "18 Mar 2022":
        df["sample_id"] = pd.to_numeric(
            df["Unnamed: 0"],
            errors="coerce"
        )

    elif date == "11 Apr 2022":
        df["sample_id"] = pd.to_numeric(
            df["code"],
            errors="coerce"
        )

    else:
        # May uses code 183–312.
        # Convert to the common 1–130 sample ID.
        df["sample_id"] = (
            pd.to_numeric(
                df["code"],
                errors="coerce"
            ) - 182
        )

    # ----------------------------------------------
    # Keep relevant columns
    # ----------------------------------------------

    required_columns = [
        "sample_id",
        "genotype",
        "near_infrared",
        "red",
        "redEdge",
        "blue",
        "EVI"
    ]

    available_columns = [
        col for col in required_columns
        if col in df.columns
    ]

    df = df[available_columns].copy()

    df["date"] = date

    # ----------------------------------------------
    # Numeric conversion
    # ----------------------------------------------

    for col in [
        "near_infrared",
        "red",
        "redEdge",
        "blue",
        "EVI"
    ]:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # ----------------------------------------------
    # Calculate NDVI
    # ----------------------------------------------

    denominator_ndvi = (
        df["near_infrared"] +
        df["red"]
    )

    df["NDVI_calculated"] = np.where(
        denominator_ndvi != 0,
        (
            df["near_infrared"] -
            df["red"]
        ) / denominator_ndvi,
        np.nan
    )

    # ----------------------------------------------
    # Calculate NDRE
    # ----------------------------------------------

    denominator_ndre = (
        df["near_infrared"] +
        df["redEdge"]
    )

    df["NDRE_calculated"] = np.where(
        denominator_ndre != 0,
        (
            df["near_infrared"] -
            df["redEdge"]
        ) / denominator_ndre,
        np.nan
    )

    # ----------------------------------------------
    # Merge ground truth
    # ----------------------------------------------

    df = df.merge(
        gt,
        on="sample_id",
        how="left"
    )

    all_data.append(df)


# --------------------------------------------------
# Combine all dates
# --------------------------------------------------

analysis_df = pd.concat(
    all_data,
    ignore_index=True
)


# --------------------------------------------------
# Sort
# --------------------------------------------------

analysis_df = analysis_df.sort_values(
    ["sample_id", "date"]
)


# --------------------------------------------------
# Save
# --------------------------------------------------

output_file = (
    "data/"
    "crop_biomass_analysis.csv"
)

analysis_df.to_csv(
    output_file,
    index=False
)


# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\nDATASET CREATED")
print("=" * 70)

print("Rows:", len(analysis_df))
print("Columns:", len(analysis_df.columns))

print("\nRows by date:")

print(
    analysis_df
    .groupby("date")
    .size()
)


print("\nGround-truth availability:")

print(
    analysis_df[
        ["yield_g", "plant_height_cm"]
    ]
    .notna()
    .sum()
)


print("\nFirst 15 rows:")

print(
    analysis_df.head(15).to_string(
        index=False
    )
)

print(
    f"\nSaved to: {output_file}"
)