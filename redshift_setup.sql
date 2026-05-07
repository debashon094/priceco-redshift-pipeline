-- DDL for Warehouse Layer
CREATE TABLE IF NOT EXISTS public.store_sales_kpi (
    store_id VARCHAR(50),
    total_revenue DOUBLE PRECISION,
    transaction_count BIGINT
);

-- Optimized Bulk Load
COPY public.store_sales_kpi 
FROM 's3://priceco-raw-data-lake/gold_redshift_final/' 
IAM_ROLE 'arn:aws:iam::721366939609:role/my-redshift-s3-role'
FORMAT AS PARQUET;