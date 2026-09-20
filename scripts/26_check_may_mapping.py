import pandas as pd


# Load March
march = pd.read_excel(
    "data/18.03.2022..xlsx",
    sheet_name="Normal"
)

# Load 16 May
may = pd.read_excel(
    "data/16.05.2022..xlsx",
    sheet_name="Normal"
)


# Add position
march["position"] = range(1, len(march) + 1)
may["position"] = range(1, len(may) + 1)


# Compare by position
comparison = pd.DataFrame({
    "march_position": march["position"],
    "march_code": march["code"],
    "march_genotype": march["genotype"],

    "may_position": may["position"],
    "may_code": may["code"],
    "may_genotype": may["genotype"]
})


comparison["genotype_match"] = (
    comparison["march_genotype"]
    .astype(str)
    .str.strip()
    ==
    comparison["may_genotype"]
    .astype(str)
    .str.strip()
)


print("\nMAY DATASET SIZE")
print("=" * 70)
print("March rows:", len(march))
print("May rows:", len(may))


print("\nGENOTYPE MISMATCHES")
print("=" * 70)

mismatches = comparison[
    ~comparison["genotype_match"]
]

print(
    mismatches.to_string(index=False)
)


print("\n\nLAST 10 MAY RECORDS")
print("=" * 70)

print(
    comparison.tail(10).to_string(index=False)
)