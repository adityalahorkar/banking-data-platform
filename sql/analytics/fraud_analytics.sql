-- Fraud analytics views.

CREATE OR REPLACE VIEW analytics.fraud_summary AS
SELECT
    dfs.fraud_status,
    COUNT(*)        AS transaction_count,
    SUM(ft.amount)  AS total_amount,
    AVG(ft.amount)  AS average_amount
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_fraud_status dfs ON ft.fraud_key = dfs.fraud_key
GROUP BY dfs.fraud_status;

CREATE OR REPLACE VIEW analytics.fraud_by_transaction_type AS
SELECT
    dtt.transaction_type,
    COUNT(*)       AS fraud_count,
    SUM(ft.amount) AS fraud_amount
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_fraud_status dfs ON ft.fraud_key = dfs.fraud_key
JOIN warehouse.dim_transaction_type dtt ON ft.transaction_type_key = dtt.transaction_type_key
WHERE dfs.fraud_status = 'Fraud'
GROUP BY dtt.transaction_type;
