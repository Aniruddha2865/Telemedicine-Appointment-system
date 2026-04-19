def validate_data(df, required_columns):
    
    # Check required columns
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Check duplicates
    if df.duplicated().sum() > 0:
        print("Warning: Duplicate rows found")

    # Check negative age
    if "age" in df.columns:
        if (df["age"] < 0).any():
            raise ValueError("Invalid data: Negative age found")

    return True