 #Merge datasets on patient_id
def merge_data(df1, df2, col1, col2):
	merged = df1.merge(df2, left_on= col1, right_on= col2)
	return merged 
