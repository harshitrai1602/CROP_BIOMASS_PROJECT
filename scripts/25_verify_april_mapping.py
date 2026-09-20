import pandas as pd


# ---------------------------------------------
# Load datasets
# ---------------------------------------------

march = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

april = pd.read_excel(
    "data/11.04.2022..xlsx",
    sheet_name="Normal"
)

may = pd.read_excel(
    "data/16.05.2022..xlsx",
    sheet_name="Normal"
)

may27 = pd.read_excel(
    "data/27.05.2022..xlsx",
    sheet_name="Normal"
)


# ---------------------------------------------
# Create comparable position numbers
# ---------------------------------------------

march["position"] = range(1, len(march) + 1)
april["position"] = range(1, len(april) + 1)
may["position"] = range(1, len(may) + 1)
may27["position"] = range(1, len(may27) + 1)


# ---------------------------------------------
# Compare genotype sequence
# ---------------------------------------------

print("\nMARCH vs APRIL")
print("=" * 70)

march_april = pd.DataFrame({
    "position": march["position"],
    "march_code": march["code"],
    "march_genotype": march["genotype"],
    "april_code": april["code"],
    "april_genotype": april["genotype"]
})

march_april["genotype_match"] = (
    march_april["march_genotype"].astype(str).str.strip()
    ==
    march_april["april_genotype"].astype(str).str.strip()
)

print(
    march_april.head(20).to_string(index=False)
)

print(
    "\nGenotype matches:",
    march_april["genotype_match"].sum(),
    "/",
    len(march_april)
)


# ---------------------------------------------
# Compare March vs May
# ---------------------------------------------

print("\n\nMARCH vs MAY")
print("=" * 70)

march_may = pd.DataFrame({
    "position": march["position"],
    "march_code": march["code"],
    "march_genotype": march["genotype"],
    "may_code": may["code"],
    "may_genotype": may["genotype"]
})

march_may["genotype_match"] = (
    march_may["march_genotype"].astype(str).str.strip()
    ==
    march_may["may_genotype"].astype(str).str.strip()
)

print(
    "\nGenotype matches:",
    march_may["genotype_match"].sum(),
    "/",
    len(march_may)
)


# ---------------------------------------------
# Compare March vs 27 May
# ---------------------------------------------

print("\n\nMARCH vs 27 MAY")
print("=" * 70)

march_may27 = pd.DataFrame({
    "position": march["position"],
    "march_code": march["code"],
    "march_genotype": march["genotype"],
    "may27_code": may27["code"],
    "may27_genotype": may27["genotype"]
})

march_may27["genotype_match"] = (
    march_may27["march_genotype"].astype(str).str.strip()
    ==
    march_may27["may27_genotype"].astype(str).str.strip()
)

print(
    "\nGenotype matches:",
    march_may27["genotype_match"].sum(),
    "/",
    len(march_may27)
)


# ---------------------------------------------
# Show mismatches for April
# ---------------------------------------------

mismatches = march_april[
    ~march_april["genotype_match"]
]

print("\n\nAPRIL MISMATCHES")
print("=" * 70)

print(
    mismatches.to_string(index=False)
)