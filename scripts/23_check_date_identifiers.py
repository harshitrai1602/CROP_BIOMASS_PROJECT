import pandas as pd

files = {
    "18 Mar 2022": "data/18.03.2022..xlsx",
    "11 Apr 2022": "data/11.04.2022..xlsx",
    "16 May 2022": "data/16.05.2022..xlsx",
    "27 May 2022": "data/27.05.2022..xlsx"
}

for date, file_path in files.items():

    df = pd.read_excel(
        file_path,
        sheet_name="Normal"
    )

    print("\n" + "=" * 80)
    print(date)
    print("=" * 80)

    print("\nColumns:")
    print(df.columns.tolist()[:15])

    print("\nFirst 10 rows of identifier-related columns:")

    possible_columns = [
        col for col in df.columns
        if (
            "id" in str(col).lower()
            or "code" in str(col).lower()
            or "mark" in str(col).lower()
            or str(col) == "Unnamed: 0"
            or "genotype" in str(col).lower()
        )
    ]

    print(
        df[possible_columns]
        .head(10)
        .to_string(index=False)
    )