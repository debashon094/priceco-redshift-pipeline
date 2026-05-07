\# Priceco Medallion Data Pipeline

\*\*Databricks Serverless to AWS Redshift\*\*



An end-to-end ELT pipeline that ingests raw e-commerce data from S3, cleans regional identifiers using PySpark, and performs a high-performance bulk load into an AWS Redshift data warehouse.



\## 🏗️ Architecture

\- \*\*Bronze:\*\* Raw ingestion via Boto3 (Bypassing Serverless S3A restrictions).

\- \*\*Silver:\*\* Regex-based cleaning (Suffix removal) and data quality filtering.

\- \*\*Gold:\*\* Aggregated store performance metrics.

\- \*\*Warehouse:\*\* Optimized S3 staging and Redshift `COPY` command integration.



\## 🛠️ Key Challenges Solved

\- \*\*Serverless Security:\*\* Bypassed \[CONFIG\_NOT\_AVAILABLE] errors by using Boto3 for ingestion and staging for warehouse loading.

\- \*\*Spectrum Metadata Error:\*\* Automated the removal of Spark-specific metadata files to ensure Redshift `COPY` compatibility.

\- \*\*Data Integrity:\*\* Handled inconsistent store IDs (TX/LA suffixes) using Spark SQL Regex.

