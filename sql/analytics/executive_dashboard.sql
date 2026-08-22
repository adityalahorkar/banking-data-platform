-- Executive dashboard views.

CREATE OR REPLACE VIEW analytics.executive_summary AS
SELECT
    COUNT(*)        AS total_transactions,
    SUM(amount)     AS total_transaction_amount,
    AVG(amount)     AS avg_transaction_amount,
    SUM(CASE WHEN fraud_key = 1 THEN 1 ELSE 0 END) AS fraud_transactions
FROM warehouse.fact_transactions;

CREATE OR REPLACE VIEW analytics.high_value_customers AS
SELECT *
FROM analytics.customer_spend_summary
WHERE total_spend > 1000000;
