-- Total records
SELECT COUNT(*) FROM patient_appointments;

-- Appointments per doctor
SELECT doctor, COUNT(*) 
FROM patient_appointments
GROUP BY doctor;

-- Patients per disease
SELECT disease, COUNT(*) 
FROM patient_appointments
GROUP BY disease;

-- Latest appointments
SELECT * 
FROM patient_appointments
ORDER BY appointment_date DESC
LIMIT 5;