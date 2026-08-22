# Step 6: build the star schema -- fact_transactions plus 4 dimension
# tables (customer, transaction type, fraud status, step).

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import settings

from pyspark.sql.functions import col, monotonically_increasing_id, when
from pipeline.step5_transform_data import get_spark


def run():
    spark = get_spark()
    spark.sparkContext.setLogLevel("ERROR")

    jdbc_url = settings.get_jdbc_url()
    props = settings.get_jdbc_properties()

    transactions_df = spark.read.jdbc(url=jdbc_url, table="raw.transactions", properties=props)

    customer_dim = (
        transactions_df.select("nameorig").distinct()
        .withColumn("customer_key", monotonically_increasing_id())
        .selectExpr("customer_key", "nameorig as customer_id")
    )

    type_dim = (
        transactions_df.select("type").distinct()
        .withColumn("transaction_type_key", monotonically_increasing_id())
        .selectExpr("transaction_type_key", "type as transaction_type")
    )

    # fraud_key holds the same 0/1 value as isfraud, renamed to match
    # fact_transactions.fraud_key and the analytics views.
    fraud_dim = (
        transactions_df.select("isfraud").distinct()
        .withColumn("fraud_status", when(transactions_df.isfraud == 1, "Fraud").otherwise("Non Fraud"))
        .withColumnRenamed("isfraud", "fraud_key")
    )

    step_dim = (
        transactions_df.select("step").distinct()
        .withColumn("step_key", monotonically_increasing_id())
        .select("step_key", "step")
    )

    print("Writing dimension tables...")
    customer_dim.write.jdbc(url=jdbc_url, table="warehouse.dim_customer", mode="overwrite", properties=props)
    type_dim.write.jdbc(url=jdbc_url, table="warehouse.dim_transaction_type", mode="overwrite", properties=props)
    fraud_dim.write.jdbc(url=jdbc_url, table="warehouse.dim_fraud_status", mode="overwrite", properties=props)
    step_dim.write.jdbc(url=jdbc_url, table="warehouse.dim_step", mode="overwrite", properties=props)

    fact_df = (
        transactions_df.alias("t")
        .join(customer_dim.alias("c"), col("t.nameorig") == col("c.customer_id"), "left")
        .join(type_dim.alias("tt"), col("t.type") == col("tt.transaction_type"), "left")
        .join(step_dim.alias("s"), col("t.step") == col("s.step"), "left")
        .join(fraud_dim.alias("f"), col("t.isfraud") == col("f.fraud_key"), "left")
        .select(
            col("c.customer_key"),
            col("tt.transaction_type_key"),
            col("f.fraud_key"),
            col("s.step_key"),
            col("t.amount"),
            col("t.oldbalanceorg"),
            col("t.newbalanceorig"),
            col("t.oldbalancedest"),
            col("t.newbalancedest"),
        )
    )

    print("Writing warehouse.fact_transactions...")
    fact_df.write.jdbc(url=jdbc_url, table="warehouse.fact_transactions", mode="overwrite", properties=props)

    print("Warehouse build done.")
    spark.stop()


if __name__ == "__main__":
    run()
