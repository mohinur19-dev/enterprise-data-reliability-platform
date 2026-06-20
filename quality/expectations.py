import pandas as pd

df = pd.read_csv("data/customers.csv")

null_count = df["customer_id"].isnull().sum()

print("Null customer_id count:", null_count)