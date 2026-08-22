# Step 7: create analytics views for reporting.
# (kpi_queries.sql is skipped -- it's ad-hoc SELECTs for manual checks.)

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pipeline.db import get_engine, run_sql_file

ANALYTICS_FILES = [
    "sql/analytics/customer_analytics.sql",
    "sql/analytics/fraud_analytics.sql",
    "sql/analytics/transaction_analytics.sql",
    "sql/analytics/executive_dashboard.sql",
]


def run():
    engine = get_engine()
    for filepath in ANALYTICS_FILES:
        print("Running", filepath)
        run_sql_file(engine, filepath)
    print("Analytics views are ready.")


if __name__ == "__main__":
    run()
