-- Curated layer: aggregate outputs from the PySpark job.

CREATE SCHEMA IF NOT EXISTS curated;

CREATE TABLE IF NOT EXISTS curated.customer_spend (
    nameorig    VARCHAR(50),
    total_spend NUMERIC
);

CREATE TABLE IF NOT EXISTS curated.fraud_by_type (
    type  VARCHAR(50),
    count BIGINT
);

CREATE TABLE IF NOT EXISTS curated.transaction_volume (
    type  VARCHAR(50),
    count BIGINT
);

CREATE TABLE IF NOT EXISTS curated.avg_transaction_amount (
    type       VARCHAR(50),
    avg_amount NUMERIC
);

CREATE TABLE IF NOT EXISTS curated.fraud_amount (
    type         VARCHAR(50),
    fraud_amount NUMERIC
);
