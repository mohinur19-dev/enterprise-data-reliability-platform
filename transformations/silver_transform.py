from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Silver").getOrCreate()

df = spark.read.option("header", True).csv("data/customers.csv")

silver_df = df.dropDuplicates()

print("Silver Layer")

silver_df.show()