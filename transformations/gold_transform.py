from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder.appName("Gold").getOrCreate()

df = spark.read.option("header", True).csv("data/customers.csv")

gold_df = df.groupBy("country").agg(count("*").alias("customer_count"))

print("Gold Layer")

gold_df.show()