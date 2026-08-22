# Data dictionary & quality checks

Source: [PaySim synthetic fraud detection dataset](https://www.kaggle.com/datasets/ealaxi/paysim1) (Kaggle).

## Columns

| Column | Type | Meaning |
|---|---|---|
| step | Integer | Simulation hour, not a real date |
| type | String | PAYMENT, TRANSFER, CASH_OUT, CASH_IN, or DEBIT |
| amount | Decimal | Transaction amount |
| nameOrig | String | Sender account ID |
| oldbalanceOrg | Decimal | Sender balance before |
| newbalanceOrig | Decimal | Sender balance after |
| nameDest | String | Receiver account ID |
| oldbalanceDest | Decimal | Receiver balance before |
| newbalanceDest | Decimal | Receiver balance after |
| isFraud | Integer | 1 if fraud, 0 if not |
| isFlaggedFraud | Integer | 1 if the source system's rule flagged it |

## Data quality checks

Run by `pipeline/step3_profile_data.py`, results saved to `data/reports/`:

1. Nulls in `type`, `amount`, `nameOrig`, `nameDest`
2. `amount > 0`
3. Duplicate rows
4. Valid transaction type values

Reports: `data_quality_summary.csv`, `missing_values_report.csv`,
`negative_amounts.csv`, `transaction_type_summary.csv`.
