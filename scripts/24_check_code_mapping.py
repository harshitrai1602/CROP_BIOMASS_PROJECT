import pandas as pd

# ---------------------------------------------
# Load March spectral data
# ---------------------------------------------

march = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# ---------------------------------------------
# Load April spectral data
# ---------------------------------------------

april = pd.read_excel(
    "data/11.04.2022..xlsx",
    sheet_name="Normal"
)

# ---------------------------------------------
# Load May spectral data
# ---------------------------------------------

may = pd.read_excel(
    "data/16.05.2022..xlsx",
    sheet_name="Normal"
)

may27 = pd.read_excel(
    "data/27.05.2022..xlsx",
    sheet_name="Normal"
)

print("\nMARCH")
print("=" * 70)

print(
    march[
        ["Unnamed: 0", "code", "genotype"]
    ].head(15).to_string(index=False)
)

print("\n\nAPRIL")
print("=" * 70)

print(
    april[
        ["code", "genotype"]
    ].head(15).to_string(index=False)
)

print("\n\n16 MAY")
print("=" * 70)

print(
    may[
        ["code", "genotype"]
    ].head(15).to_string(index=False)
)

print("\n\n27 MAY")
print("=" * 70)

print(
    may27[
        ["code", "genotype"]
    ].head(15).to_string(index=False)
)

# ---------------------------------------------
# Compare code sets
# ---------------------------------------------

march_codes = set(
    pd.to_numeric(
        march["code"],
        errors="coerce"
    ).dropna()
)

april_codes = set(
    pd.to_numeric(
        april["code"],
        errors="coerce"
    ).dropna()
)

may_codes = set(
    pd.to_numeric(
        may["code"],
        errors="coerce"
    ).dropna()
)

may27_codes = set(
    pd.to_numeric(
        may27["code"],
        errors="coerce"
    ).dropna()
)

print("\n\nCODE SET COMPARISON")
print("=" * 70)

print("March codes :", len(march_codes))
print("April codes :", len(april_codes))
print("May codes   :", len(may_codes))
print("May27 codes :", len(may27_codes))

print("\nMarch ∩ April:", len(march_codes & april_codes))
print("March ∩ May  :", len(march_codes & may_codes))
print("March ∩ May27:", len(march_codes & may27_codes))

print("\nMarch codes not in May:")
print(sorted(march_codes - may_codes))

print("\nMay codes not in March:")
print(sorted(may_codes - march_codes))