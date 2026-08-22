# Shared DB connection helper used by every pipeline step.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import settings

from sqlalchemy import create_engine, text


def get_engine():
    return create_engine(settings.get_db_url())


def run_sql_file(engine, filepath):
    """Read a .sql file and run each statement in it."""
    with open(filepath) as f:
        sql_text = f.read()

    statements = [s.strip() for s in sql_text.split(";") if s.strip()]

    with engine.connect() as conn:
        for statement in statements:
            conn.execute(text(statement))
        conn.commit()
