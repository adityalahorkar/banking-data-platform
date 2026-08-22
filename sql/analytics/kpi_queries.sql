-- Ad-hoc queries for manually checking the data. Not run automatically.

SELECT SUM(amount) AS total_revenue FROM warehouse.fact_transactions;

SELECT SUM(amount) AS total_fraud_amount
FROM warehouse.fact_transactions WHERE fraud_key = 1;

SELECT MAX(amount) AS largest_transaction FROM warehouse.fact_transactions;

SELECT * FROM analytics.executive_summary;
SELECT * FROM analytics.fraud_summary;
SELECT * FROM analytics.top_10_customers;
