import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="telemedicine_db",
        user="postgres",
        password="ritan5#sql"
    )
    return conn