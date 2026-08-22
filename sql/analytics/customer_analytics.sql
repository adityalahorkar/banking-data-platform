-- Customer analytics views.

CREATE OR REPLACE VIEW analytics.customer_spend_summary AS
SELECT
    dc.customer_key,
    dc.customer_id,
    COUNT(*)        AS total_transactions,
    SUM(ft.amount)  AS total_spend,
    AVG(ft.amount)  AS avg_transaction_amount
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_customer dc ON ft.customer_key = dc.customer_key
GROUP BY dc.customer_key, dc.customer_id;

CREATE OR REPLACE VIEW analytics.top_10_customers AS
SELECT *
FROM analytics.customer_spend_summary
ORDER BY total_spend DESC
LIMIT 10;
