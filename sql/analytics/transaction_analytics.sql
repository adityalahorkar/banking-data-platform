-- Transaction volume and type analytics views.

CREATE OR REPLACE VIEW analytics.transaction_type_summary AS
SELECT
    dtt.transaction_type,
    COUNT(*)       AS transaction_count,
    SUM(ft.amount) AS total_amount,
    AVG(ft.amount) AS average_amount
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_transaction_type dtt ON ft.transaction_type_key = dtt.transaction_type_key
GROUP BY dtt.transaction_type;
