import boto3
import pandas as pd
import io
from pyspark.sql.functions import col, regexp_replace, trim, current_timestamp, sum, count

# Config
BUCKET = "priceco-raw-data-lake"
TARGET_TABLE = "priceco_catalog.bronze_layer.raw_data_1000"

def ingest_bronze():
    # Uses Boto3 bridge for Serverless compatibility
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=BUCKET, Prefix="excel_uploads/")
    # ... (Insert the Boto3 logic we used here)
    print("Bronze Layer Ingested.")

def transform_silver():
    silver_df = (spark.table(TARGET_TABLE)
        .withColumn("store_id", trim(regexp_replace(col("store_id"), "TX|LA", "")))
        .filter(col("price") > 0))
    silver_df.write.format("delta").mode("overwrite").saveAsTable("priceco_catalog.silver_layer.clean_data")

def export_to_redshift():
    # Stage to S3 and clean metadata
    path = f"s3a://{BUCKET}/gold_redshift_final/"
    spark.table("gold_metrics").coalesce(1).write.parquet(path)
    
    # Remove metadata files
    for f in dbutils.fs.ls(path):
        if f.name.startswith("_"):
            dbutils.fs.rm(f.path)
