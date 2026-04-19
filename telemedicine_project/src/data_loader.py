import pandas as pd 
print("pandas imported succesfully")

#Read CSV files
def load_csv(file_path):
	df = pd.read_csv(file_path)
	return df 
patients = load_csv("data/raw/patients.csv")
appointments = load_csv("data/raw/appointments.csv")

print("Patients Data :" )
print(patients.head())

print("\n Appointments Data:")
print(appointments.head())

#Info about datasets 
print("\n ---Patients info ---")
patients.info()

print("\n ---Appointments info---")
appointments.info()

#DataTypes 
print("\n ---Patients Dtypes ---\n", patients.dtypes)
print("\n ---Appointments Dtypes---\n", appointments.dtypes)