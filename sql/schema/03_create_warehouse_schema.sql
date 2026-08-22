-- Warehouse layer: star schema (fact + dimension tables).

CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE IF NOT EXISTS warehouse.dim_customer (
    customer_key BIGINT,
    customer_id  VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS warehouse.dim_transaction_type (
    transaction_type_key BIGINT,
    transaction_type     VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS warehouse.dim_fraud_status (
    fraud_key    BIGINT,
    fraud_status VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS warehouse.dim_step (
    step_key BIGINT,
    step     INTEGER
);

CREATE TABLE IF NOT EXISTS warehouse.fact_transactions (
    customer_key          BIGINT,
    transaction_type_key  BIGINT,
    fraud_key             BIGINT,
    step_key              BIGINT,
    amount                NUMERIC(18, 2),
    oldbalanceorg         NUMERIC(18, 2),
    newbalanceorig        NUMERIC(18, 2),
    oldbalancedest        NUMERIC(18, 2),
    newbalancedest        NUMERIC(18, 2)
);
