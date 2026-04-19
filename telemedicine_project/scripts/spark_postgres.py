from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, max, min, when

# Create Spark session
spark = SparkSession.builder \
    .appName("TelemedicinePostgresAdvancedAnalytics") \
    .config("spark.jars", "jars/postgresql-42.7.3.jar") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# PostgreSQL connection
url = "jdbc:postgresql://localhost:5432/telemedicine_db"

properties = {
    "user": "postgres",
    "password": "ritan5#sql",  
    "driver": "org.postgresql.Driver"
}

# Load data
df = spark.read.jdbc(
    url=url,
    table="patient_appointments",
    properties=properties
)

# 1. Total patients
total_patients = df.count()
print("Total Patients:", total_patients)

# 2. Patients per doctor
q1 = df.groupBy("doctor").agg(count("*").alias("total_patients"))

# 3. Top doctors
q2 = q1.orderBy(col("total_patients").desc())

# 4. Disease distribution
q3 = df.groupBy("disease").agg(count("*").alias("cases"))

# 5. Most common diseases
q4 = q3.orderBy(col("cases").desc())

# 6. Appointments per day
q5 = df.groupBy("appointment_date").agg(count("*").alias("appointments"))

# 7. Peak appointment day
q6 = q5.orderBy(col("appointments").desc())

# 8. Gender distribution
q7 = df.groupBy("gender").agg(count("*").alias("count"))

# 9. Gender-wise disease distribution
q8 = df.groupBy("gender", "disease").agg(count("*").alias("count"))

# 10. Average age per disease
q9 = df.groupBy("disease").agg(avg("age").alias("avg_age"))

# 11. Doctor workload per day
q10 = df.groupBy("doctor", "appointment_date").agg(count("*").alias("appointments"))

# 12. Age group analysis
df = df.withColumn(
    "age_group",
    when(col("age") < 18, "Child")
    .when((col("age") >= 18) & (col("age") <= 40), "Adult")
    .otherwise("Senior")
)

q11 = df.groupBy("age_group").agg(count("*").alias("patients"))

# 13. Min & Max age per disease
q12 = df.groupBy("disease").agg(
    min("age").alias("min_age"),
    max("age").alias("max_age")
)


q1.coalesce(1).write.mode("overwrite").csv("data/output_postgres/patients_per_doctor", header=True)
q2.coalesce(1).write.mode("overwrite").csv("data/output_postgres/top_doctors", header=True)
q3.coalesce(1).write.mode("overwrite").csv("data/output_postgres/disease_distribution", header=True)
q4.coalesce(1).write.mode("overwrite").csv("data/output_postgres/top_diseases", header=True)
q5.coalesce(1).write.mode("overwrite").csv("data/output_postgres/appointments_per_day", header=True)
q6.coalesce(1).write.mode("overwrite").csv("data/output_postgres/peak_days", header=True)
q7.coalesce(1).write.mode("overwrite").csv("data/output_postgres/gender_distribution", header=True)
q8.coalesce(1).write.mode("overwrite").csv("data/output_postgres/gender_disease", header=True)
q9.coalesce(1).write.mode("overwrite").csv("data/output_postgres/avg_age_disease", header=True)
q10.coalesce(1).write.mode("overwrite").csv("data/output_postgres/doctor_daily_load", header=True)
q11.coalesce(1).write.mode("overwrite").csv("data/output_postgres/age_groups", header=True)
q12.coalesce(1).write.mode("overwrite").csv("data/output_postgres/min_max_age_disease", header=True)

print("All PostgreSQL Spark analyses completed and saved.")

spark.stop()