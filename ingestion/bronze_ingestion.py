from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Bronze Layer")
    .getOrCreate()
)

df = spark.read.option("header", True).csv("data/customers.csv")

print("Raw Data")

df.show()