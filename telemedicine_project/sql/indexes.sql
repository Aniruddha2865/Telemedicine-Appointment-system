-- Index on doctor
CREATE INDEX idx_doctor
ON patient_appointments (doctor);

-- Index on disease
CREATE INDEX idx_disease
ON patient_appointments (disease);

-- Index on appointment_date
CREATE INDEX idx_date
ON patient_appointments (appointment_date);