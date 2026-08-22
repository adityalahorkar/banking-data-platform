# Step 3: profile the raw CSV and save data quality reports.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import settings

import pandas as pd

REPORTS_DIR = "data/reports"


def run():
    df = pd.read_csv(settings.RAW_DATA_PATH)

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Transaction types:", df["type"].unique())

    os.makedirs(REPORTS_DIR, exist_ok=True)

    df.isnull().sum().rename("missing_count").to_csv(f"{REPORTS_DIR}/missing_values_report.csv")
    df[df["amount"] < 0].to_csv(f"{REPORTS_DIR}/negative_amounts.csv", index=False)
    df["type"].value_counts().rename("count").to_csv(f"{REPORTS_DIR}/transaction_type_summary.csv")

    pd.DataFrame([{
        "total_rows": len(df),
        "total_columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "zero_or_negative_amounts": int((df["amount"] <= 0).sum()),
    }]).to_csv(f"{REPORTS_DIR}/data_quality_summary.csv", index=False)

    print(f"Data quality reports saved to {REPORTS_DIR}/")
    return df


if __name__ == "__main__":
    run()
