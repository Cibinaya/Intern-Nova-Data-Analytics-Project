import pandas as pd
file_path = "StudentCount_PuneRegion_.csv"
df=pd.read_csv(file_path)

print("1.DATASET SHAPE")
print(f"Total Schools(Rows):{df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

print("\n 2. COLUMNS & DATA TYPES")
print(df.dtypes)

print("\n 3. MISSING VALUE COUNT")
missing_values= df.isnull().sum()
print(missing_values[missing_values>0])

print("\n 4. DUPLICATE RECORDS ")
duplicates= df.duplicated().sum()
print(f"Total Duplicate Rows : {duplicates}")

standard_cols = [f'Std_{i}' for i in range (1,13)]
df[standard_cols]= df[standard_cols].fillna(0)

print("\n 5. AFTER HANDLING MISSING VALUES")
print("missing values in standard after imputation:", df[standard_cols].isnull().sum().sum())
print("Data preparation Completed Successfully!")