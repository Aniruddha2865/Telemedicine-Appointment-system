import pandas as pd
from src.data_loader import load_csv
from src.data_cleaner import clean_data
from src.data_merger import merge_data
from src.data_validator import validate_data
from src.logger import setup_logger
from src.db_connector import get_connection
from src.db_writer import insert_data

logger = setup_logger()
logger.info("Loading data...")
patients = load_csv("data/raw/patients.csv")
appointments = load_csv("data/raw/appointments.csv")

logger.info("Validating data...")
validate_data(patients, ["id", "name", "age"])
validate_data(appointments, ["appointment_id", "patient_id"])

logger.info("Cleaning data...")
patients = clean_data(patients)
appointments = clean_data(appointments)

logger.info("Merging data ...")
merged_data = merge_data(patients, appointments, "id", "patient_id")

logger.info("Saving data...")
merged_data.to_csv("data/processed/merged_data.csv", index=False)

merged_data.rename(columns={"date": "appointment_date"}, inplace=True)

merged_data['appointment_date'] = pd.to_datetime(
    merged_data['appointment_date'],
    format='%d-%m-%Y',
    errors='coerce'
)
merged_data['age'] = merged_data['age'].astype(int)

logger.info("Pipeline executed successfully")

conn = get_connection()
print("✅ Connected to PostgreSQL")
conn.close()

insert_data(merged_data)