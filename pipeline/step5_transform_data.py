# Step 5: PySpark transformations -- customer spend, fraud, and volume
# aggregates, written to the curated schema.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import settings

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum as spark_sum


def get_spark():
    return (
        SparkSession.builder.appName(settings.SPARK_APP_NAME)
        .master(settings.SPARK_MASTER)
        .config("spark.driver.memory", settings.SPARK_DRIVER_MEMORY)
        .config("spark.executor.memory", settings.SPARK_EXECUTOR_MEMORY)
        .config("spark.jars", settings.JDBC_JAR_PATH)
        .getOrCreate()
    )


def run():
    spark = get_spark()
    spark.sparkContext.setLogLevel("ERROR")

    jdbc_url = settings.get_jdbc_url()
    props = settings.get_jdbc_properties()

    transactions_df = spark.read.jdbc(url=jdbc_url, table="raw.transactions", properties=props)
    transactions_df.cache()
    print("Total rows:", transactions_df.count())

    customer_spend_df = transactions_df.groupBy("nameorig").agg(spark_sum("amount").alias("total_spend"))

    fraud_df = transactions_df.filter(transactions_df.isfraud == 1)
    fraud_by_type_df = fraud_df.groupBy("type").count()
    fraud_amount_df = fraud_df.groupBy("type").agg(spark_sum("amount").alias("fraud_amount"))

    transaction_volume_df = transactions_df.groupBy("type").count()
    avg_transaction_df = transactions_df.groupBy("type").agg(avg("amount").alias("avg_amount"))

    outputs = {
        "curated.customer_spend": customer_spend_df,
        "curated.fraud_by_type": fraud_by_type_df,
        "curated.transaction_volume": transaction_volume_df,
        "curated.avg_transaction_amount": avg_transaction_df,
        "curated.fraud_amount": fraud_amount_df,
    }

    for table_name, df in outputs.items():
        print("Writing", table_name)
        df.write.jdbc(url=jdbc_url, table=table_name, mode="overwrite", properties=props)

    print("Curated layer done.")
    spark.stop()


if __name__ == "__main__":
    run()
