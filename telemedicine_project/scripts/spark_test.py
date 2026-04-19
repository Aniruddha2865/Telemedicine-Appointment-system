from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("TelemedicineSparkTest") \
    .getOrCreate()

# Create sample data
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Define columns
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show data
df.show()

# Stop Spark
spark.stop()