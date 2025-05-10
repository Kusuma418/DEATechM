from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("MergeDirtyCSVs").getOrCreate()

# Input and Output GCS Paths
input_path = "gs://kusuma-project/input/bank_transactions/*"
output_path = "gs://kusuma-project/output/merged_transactions/"

# Read all CSVs from the input path
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Optional: Drop rows where all values are null (common in dirty data)
df_clean = df.dropna(how="all")

# Optional: Drop duplicates if necessary
df_clean = df_clean.dropDuplicates()

# Save merged & cleaned CSV to output GCS path
df_clean.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

# Stop the Spark session
spark.stop()