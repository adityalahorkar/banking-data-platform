# Central configuration, loaded from environment variables (.env).

import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "banking_platform")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


def get_db_url(dbname=None):
    """SQLAlchemy connection string. Pass dbname='postgres' to connect to
    the default maintenance database (used to create our DB if missing)."""
    dbname = dbname or DB_NAME
    safe_password = quote_plus(DB_PASSWORD)
    return f"postgresql+psycopg2://{DB_USER}:{safe_password}@{DB_HOST}:{DB_PORT}/{dbname}"


def get_jdbc_url():
    return f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}"


def get_jdbc_properties():
    return {"user": DB_USER, "password": DB_PASSWORD, "driver": "org.postgresql.Driver"}


SPARK_APP_NAME = os.getenv("SPARK_APP_NAME", "BankingDataPlatform")
SPARK_MASTER = os.getenv("SPARK_MASTER", "local[*]")
SPARK_DRIVER_MEMORY = os.getenv("SPARK_DRIVER_MEMORY", "4g")
SPARK_EXECUTOR_MEMORY = os.getenv("SPARK_EXECUTOR_MEMORY", "2g")
JDBC_JAR_PATH = os.getenv("SPARK_JDBC_JAR", "jars/postgresql-42.7.3.jar")

RAW_DATA_PATH = "data/raw/transactions.csv"
