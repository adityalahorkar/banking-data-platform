# Step 4: load the raw CSV into raw.transactions, as-is (no cleaning).

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import settings
from pipeline.db import get_engine

import pandas as pd

COLUMN_RENAME_MAP = {
    "nameOrig": "nameorig",
    "oldbalanceOrg": "oldbalanceorg",
    "newbalanceOrig": "newbalanceorig",
    "nameDest": "namedest",
    "oldbalanceDest": "oldbalancedest",
    "newbalanceDest": "newbalancedest",
    "isFraud": "isfraud",
    "isFlaggedFraud": "isflaggedfraud",
}


def run():
    df = pd.read_csv(settings.RAW_DATA_PATH)
    df = df.rename(columns=COLUMN_RENAME_MAP)

    engine = get_engine()
    df.to_sql("transactions", engine, schema="raw", if_exists="append", index=False, chunksize=10_000)

    print(f"Loaded {len(df)} rows into raw.transactions")


if __name__ == "__main__":
    run()
