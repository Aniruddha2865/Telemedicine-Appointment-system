#Handling missing values 
def clean_data(df):
	df = df.copy()
	for col in df.select_dtypes(include=['int64','float64']):
		df[col] = df[col].fillna(df[col].mean())
	
	for col in df.select_dtypes(include=['object']):
		df[col] = df[col].fillna("Unknown")
	return df
