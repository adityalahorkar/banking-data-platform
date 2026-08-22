# Checks the database is reachable and the schemas exist.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pipeline.db import get_engine


def test_connection_works():
    engine = get_engine()
    with engine.connect() as conn:
        assert conn.exec_driver_sql("SELECT 1;").scalar() == 1


def test_schemas_exist():
    engine = get_engine()
    expected = {"raw", "curated", "warehouse", "analytics"}
    with engine.connect() as conn:
        rows = conn.exec_driver_sql("SELECT schema_name FROM information_schema.schemata;")
        existing = {row[0] for row in rows}
    assert not (expected - existing)
