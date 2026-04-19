from psycopg2.extras import execute_values
from src.db_connector import get_connection

def insert_data(df):
    conn = get_connection()
    cursor = conn.cursor()

    # convert dataframe to list of tuples
    data_tuples = [
        (
            row.id,
            row.name,
            row.age,
            row.gender,
            row.disease,
            row.appointment_id,
            row.patient_id,
            row.appointment_date,
            row.doctor
        )
        for row in df.itertuples(index=False)
    ]

    query = """
        INSERT INTO patient_appointments (
            id, name, age, gender, disease,
            appointment_id, patient_id, appointment_date, doctor
        ) VALUES %s
        ON CONFLICT (appointment_id) DO NOTHING
    """

    execute_values(cursor, query, data_tuples)

    conn.commit()
    cursor.close()
    conn.close()

    print("Bulk insert completed")