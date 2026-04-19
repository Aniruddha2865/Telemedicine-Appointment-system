CREATE TABLE patient_appointments (
    id INT,
    name TEXT,
    age INT,
    gender TEXT,
    disease TEXT,
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    appointment_date DATE,
    doctor TEXT
);