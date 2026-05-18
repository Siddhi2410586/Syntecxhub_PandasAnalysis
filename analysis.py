import pandas as pd

# 1. Read CSV into DataFrame
df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')
print("=== DATA LOADED ===")
print("Total rows:", len(df))

# 2. Inspect head/tail/types
print("\nFirst 5 rows:")
print(df.head())
print("\nData Types:")
print(df.dtypes)

# 3. Summary stats - mean, median, min, max, count
print