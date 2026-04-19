from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder \
    .appName("TelemedicineSparkSQL") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv(
    "data/processed/merged_data.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn("date", to_date(col("date"), "dd-MM-yyyy"))

# Register table
df.createOrReplaceTempView("telemedicine")

# SQL Queries
doctor_sql = spark.sql("""
    SELECT doctor, COUNT(*) AS total_patients
    FROM telemedicine
    GROUP BY doctor
""")

disease_sql = spark.sql("""
    SELECT disease, COUNT(*) AS count
    FROM telemedicine
    GROUP BY disease
""")

date_sql = spark.sql("""
    SELECT date, COUNT(*) AS appointments
    FROM telemedicine
    GROUP BY date
    ORDER BY date
""")

# Show
doctor_sql.show()
disease_sql.show()
date_sql.show()

# Save
doctor_sql.coalesce(1).write.mode("overwrite").csv("data/output_sql/doctor_analysis", header=True)
disease_sql.coalesce(1).write.mode("overwrite").csv("data/output_sql/disease_analysis", header=True)
date_sql.coalesce(1).write.mode("overwrite").csv("data/output_sql/date_analysis", header=True)

spark.stop()