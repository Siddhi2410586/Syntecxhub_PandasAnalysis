# Syntecxhub - Pandas CSV Reader & Basic Analysis

## Task 2: Data Science Internship Requirements

### **Requirements Completed:**
1. **Read CSV into DataFrame** - Loaded `sales_data_sample.csv` with 2823 rows using `pd.read_csv()`
2. **Inspect Data** - `df.head()`, `df.tail()`, `df.dtypes` 
3. **Summary Statistics** - `df['SALES'].describe()` for count, mean, median, min, max
4. **Filter Rows & Select Columns** - Filtered SALES > 5000, selected ORDERNUMBER, ORDERDATE, SALES, COUNTRY, STATUS
5. **Save Results** - Exported filtered data to `high_value_sales.csv`

### **How to Run**
```bash
py -m pip install pandas
py analysis.py