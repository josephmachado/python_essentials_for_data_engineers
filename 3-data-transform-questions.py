print(
    "################################################################################"
)
print("Use standard python libraries to do the transformations")
print(
    "################################################################################"
)

# Question: How do you read data from a CSV file at ./data/sample_data.csv into a list of dictionaries?

# Question: How do you remove duplicate rows based on customer ID?

# Question: How do you handle missing values by replacing them with 0?

# Question: How do you remove outliers such as age > 100 or purchase amount > 1000?

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male)?

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name columns?

# Question: How do you calculate the total purchase amount by Gender?

# Question: How do you calculate the average purchase amount by Age group?
# assume age_groups is the grouping we want
# hint: Why do we convert to float?
age_groups = {"18-30": [], "31-40": [], "41-50": [], "51-60": [], "61-70": []}

# Question: How do you print the results for total purchase amount by Gender and average purchase amount by Age group?
your_total_purchase_amount_by_gender = {} # your results should be assigned to this variable
average_purchase_by_age_group = {} # your results should be assigned to this variable

print(f"Total purchase amount by Gender: {your_total_purchase_amount_by_gender}")
print(f"Average purchase amount by Age group: {average_purchase_by_age_group}")

print(
    "################################################################################"
)
print("Use DuckDB to do the transformations")
print(
    "################################################################################"
)

# Question: How do you connect to DuckDB and load data from a CSV file into a DuckDB table?
# Connect to DuckDB and load data

# Read data from CSV file into DuckDB table

# Question: How do you remove duplicate rows based on customer ID in DuckDB?

# Question: How do you handle missing values by replacing them with 0 in DuckDB?

# Question: How do you remove outliers (e.g., age > 100 or purchase amount > 1000) in DuckDB?

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male) in DuckDB?

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name columns in DuckDB?

# Question: How do you calculate the total purchase amount by Gender in DuckDB?

# Question: How do you calculate the average purchase amount by Age group in DuckDB?

# Question: How do you print the results for total purchase amount by Gender and average purchase amount by Age group in DuckDB?
print("====================== Results ======================")
print("Total purchase amount by Gender:")
print("Average purchase amount by Age group:")
