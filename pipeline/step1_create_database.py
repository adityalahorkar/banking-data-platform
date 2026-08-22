# Step 1: create the database if it doesn't already exist.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import settings

from sqlalchemy import create_engine, text


def run():
    engine = create_engine(settings.get_db_url(dbname="postgres"))
    engine = engine.execution_options(isolation_level="AUTOCOMMIT")

    with engine.connect() as conn:
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :name"),
            {"name": settings.DB_NAME},
        ).scalar()

        if exists:
            print(f"Database '{settings.DB_NAME}' already exists.")
        else:
            conn.execute(text(f'CREATE DATABASE "{settings.DB_NAME}"'))
            print(f"Created database '{settings.DB_NAME}'.")


if __name__ == "__main__":
    run()
