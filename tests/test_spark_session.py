# Checks PySpark is installed and a local session starts.

from pyspark.sql import SparkSession


def test_spark_starts():
    spark = SparkSession.builder.appName("SmokeTest").master("local[1]").getOrCreate()
    assert spark.version is not None
    spark.stop()
