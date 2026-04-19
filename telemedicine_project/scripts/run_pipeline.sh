#!/bin/bash

echo "======================================"
echo "Starting Telemedicine Data Pipeline"
echo "======================================"

# Step 1: Python ETL
echo "Step 1: Running Data Processing (ETL)..."
python3 scripts/process_data.py

if [ $? -ne 0 ]; then
    echo "ETL FAILED "
    exit 1
fi

# Step 2: Spark CSV Analytics
echo "Step 2: Running Spark CSV Analytics..."
python3 scripts/spark_load.py

if [ $? -ne 0 ]; then
    echo "Spark CSV FAILED "
    exit 1
fi

# Step 3: Spark PostgreSQL Analytics
echo "Step 3: Running Spark PostgreSQL Analytics..."
python3 scripts/spark_postgres.py

if [ $? -ne 0 ]; then
    echo "Spark PostgreSQL FAILED "
    exit 1
fi

# Step 4: Upload outputs to S3
echo "Step 4: Uploading outputs to S3..."

aws s3 cp data/output_sql/ s3://telemedicine-data-aniruddha/output_sql/ --recursive
aws s3 cp data/output_postgres/ s3://telemedicine-data-aniruddha/output_postgres/ --recursive

if [ $? -ne 0 ]; then
    echo "S3 Upload FAILED "
    exit 1
fi

echo "======================================"
echo "Pipeline completed successfully"
echo "======================================"