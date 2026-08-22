# Step 2: create schemas and tables from sql/schema/.

import sys
import os
import glob

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pipeline.db import get_engine, run_sql_file


def run():
    engine = get_engine()
    for filepath in sorted(glob.glob("sql/schema/*.sql")):
        print("Running", filepath)
        run_sql_file(engine, filepath)
    print("Schemas and tables are ready.")


if __name__ == "__main__":
    run()
