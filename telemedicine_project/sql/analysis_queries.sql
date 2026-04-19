-- 1. Total number of records
SELECT COUNT(*) AS total_records
FROM patient_appointments;

-- 2. Number of appointments per doctor
SELECT doctor, COUNT(*) AS total_appointments
FROM patient_appointments
GROUP BY doctor
ORDER BY total_appointments DESC;

-- 3. Number of patients per disease
SELECT disease, COUNT(*) AS patient_count
FROM patient_appointments
GROUP BY disease
ORDER BY patient_count DESC;

-- 4. Average age of patients
SELECT AVG(age) AS average_age
FROM patient_appointments;

-- 5. Gender distribution
SELECT gender, COUNT(*) AS count
FROM patient_appointments
GROUP BY gender;

-- 6. Latest 5 appointments
SELECT *
FROM patient_appointments
ORDER BY appointment_date DESC
LIMIT 5;

-- 7. Appointments per date
SELECT appointment_date, COUNT(*) AS total
FROM patient_appointments
GROUP BY appointment_date
ORDER BY appointment_date;