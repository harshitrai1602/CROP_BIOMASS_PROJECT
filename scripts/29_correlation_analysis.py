import pandas as pd
import numpy as np


# --------------------------------------------------
# Load clean dataset
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
# Features
# --------------------------------------------------

features = [
    "NDVI_calculated",
    "NDRE_calculated",
    "EVI"
]

targets = [
    "yield_g",
    "plant_height_cm"
]


# --------------------------------------------------
# Calculate correlations
# --------------------------------------------------

results = []


for date in date_order:

    date_df = df[
        df["date"] == date
    ].copy()

    for feature in features:

        for target in targets:

            # Keep only valid pairs
            valid = date_df[
                [feature, target]
            ].dropna()

            if len(valid) >= 2:

                correlation = (
                    valid[feature]
                    .corr(valid[target])
                )

            else:

                correlation = np.nan

            results.append({
                "date": date,
                "feature": feature,
                "target": target,
                "n": len(valid),
                "pearson_r": correlation
            })


# --------------------------------------------------
# Create result table
# --------------------------------------------------

results_df = pd.DataFrame(results)


print("\nDATE-WISE CORRELATION ANALYSIS")
print("=" * 80)

print(
    results_df.to_string(
        index=False
    )
)


# --------------------------------------------------
# Save results
# --------------------------------------------------

results_df.to_csv(
    "data/correlation_results.csv",
    index=False
)

print(
    "\nSaved to: data/correlation_results.csv"
)