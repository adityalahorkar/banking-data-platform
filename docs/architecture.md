# Architecture

## Pipeline

```text
Kaggle dataset
      |
      v
Create database + schemas         (pipeline/step1, step2)
      |
      v
Profile raw data                  (pipeline/step3)
      |
      v
Load into PostgreSQL raw layer    (pipeline/step4)
      |
      v
PySpark transformations           (pipeline/step5)
      |
      v
Build warehouse (star schema)     (pipeline/step6)
      |
      v
Create analytics views            (pipeline/step7)
      |
      v
Power BI dashboard
```

Run all 7 steps with `python run_pipeline.py`.

## Layers

| Layer | Tech | Purpose |
|---|---|---|
| Landing zone | `data/raw/` | Source CSV, untouched |
| Raw | Postgres (`raw`) | Exact copy of source data |
| Transformation | PySpark | Cleans and aggregates |
| Curated | Postgres (`curated`) | PySpark output |
| Warehouse | Postgres (`warehouse`) | Star schema: fact + dimensions |
| Analytics | Postgres views (`analytics`) | Views Power BI queries |
| Orchestration | Airflow (optional) | Same steps, on a schedule |

## Star schema

```text
                 dim_customer
                       |
dim_transaction_type --- fact_transactions --- dim_step
                       |
                 dim_fraud_status
```

- `fact_transactions` -- one row per transaction: amounts + foreign keys.
- `dim_customer` -- one row per unique sender account.
- `dim_transaction_type` -- the 5 transaction types.
- `dim_fraud_status` -- Fraud / Non Fraud.
- `dim_step` -- source data's simulation hour (not a real date).

See `sql/schema/03_create_warehouse_schema.sql` for table definitions and
`pipeline/step6_build_warehouse.py` for the build logic.
