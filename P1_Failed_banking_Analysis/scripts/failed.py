from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim

spark = SparkSession.builder.appName("FilterFailed").getOrCreate()

# Load cleaned data
df = spark.read.option("header", True).csv("gs://kusuma-project/output/merged_transactions/part-00000-41b45906-cb17-48f4-8fce-e80e9fa8fd16-c000.csv")

# Normalize status column
# df_clean = df.withColumn("status", lower(trim(col("status"))))

# Filter rows where status = 'failure'
failed_df = df.filter(col("status") == "FAILED")

# Save the failed transactions
failed_df.write.mode("overwrite").option("header", True).csv("gs://kusuma-project/output_failed_data/")