"""
Cleaning:

1. Remove any duplicate rows based on customer ID or any other unique identifier.
2. Handle missing values in any of the columns, such as replacing them with the mean or median for numeric columns or the mode for categorical columns.
3. Check for and handle outliers in the Age and Purchase_Amount columns.
4. Standardize the format of dates in the Purchase_Date column if they are not already consistent.

Transformation:

1. Convert the Gender column to a binary format (e.g., 0 for Female and 1 for Male).
2. Split the Customer_Name column into separate First_Name and Last_Name columns.
3. Extract additional features from the Purchase_Date column, such as day of the week or month, to analyze purchase patterns over time.

Aggregation:

1. Calculate summary statistics such as mean, median, minimum, and maximum values for numeric columns like Age and Purchase_Amount.
2. Group the data by Gender and calculate the total purchase amount for each gender group.
3. Aggregate data by Age ranges (e.g., 18-30, 31-40, etc.) and calculate the average purchase amount for each age group.
"""

import csv
from collections import defaultdict

# Read data from CSV file
print("====================== Reading data from CSV file ======================")
data = []
with open("./data/sample_data.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Remove duplicate rows based on customer ID
print("====================== Removing duplicate rows ======================")
data_unique = []
customer_ids_seen = set()
for row in data:
    if row["Customer_ID"] not in customer_ids_seen:
        data_unique.append(row)
        customer_ids_seen.add(row["Customer_ID"])
    else:
        print(f'duplicate customer id {row["Customer_ID"]}')

# Handle missing values (replace with 0 for simplicity)
print("====================== Handling missing values ======================")
for row in data_unique:
    if not row["Age"]:
        print(f'Customer {row["Customer_Name"]} does not have Age value')
        row["Age"] = 0
    if not row["Purchase_Amount"]:
        row["Purchase_Amount"] = 0.0

# Remove outliers (e.g., age > 100 or purchase amount > 1000)
print("====================== Removing outliers ======================")
data_cleaned = [
    row
    for row in data_unique
    if int(row["Age"]) <= 100 and float(row["Purchase_Amount"]) <= 1000
]

# Convert Gender column to binary format (0 for Female, 1 for Male)
print("====================== Converting Gender column ======================")
for row in data_cleaned:
    if row["Gender"] == "Female":
        row["Gender"] = 0
    elif row["Gender"] == "Male":
        row["Gender"] = 1

# Split Customer_Name into First_Name and Last_Name columns
print("====================== Splitting Customer_Name ======================")
for row in data_cleaned:
    first_name, last_name = row["Customer_Name"].split(" ", 1)
    row["First_Name"] = first_name
    row["Last_Name"] = last_name
    del row["Customer_Name"]

# Calculate total purchase amount by Gender
print(
    "====================== Calculating total purchase amount by Gender ======================"
)
total_purchase_by_gender = defaultdict(float)
for row in data_cleaned:
    total_purchase_by_gender[row["Gender"]] += float(row["Purchase_Amount"])

# Calculate average purchase amount by Age group
print(
    "====================== Calculating average purchase amount by Age group ======================"
)
age_groups = {"18-30": [], "31-40": [], "41-50": [], "51-60": [], "61-70": []}
for row in data_cleaned:
    age = int(row["Age"])
    if age <= 30:
        age_groups["18-30"].append(float(row["Purchase_Amount"]))
    elif age <= 40:
        age_groups["31-40"].append(float(row["Purchase_Amount"]))
    elif age <= 50:
        age_groups["41-50"].append(float(row["Purchase_Amount"]))
    elif age <= 60:
        age_groups["51-60"].append(float(row["Purchase_Amount"]))
    else:
        age_groups["61-70"].append(float(row["Purchase_Amount"]))

average_purchase_by_age_group = {
    group: sum(amounts) / len(amounts) for group, amounts in age_groups.items()
}

# Print results
print("====================== Results ======================")
print("Total purchase amount by Gender:", total_purchase_by_gender)
print("Average purchase amount by Age group:", average_purchase_by_age_group)

print(
    "################################################################################"
)
print("Use DuckDB to do the transformations")
print(
    "################################################################################"
)

import duckdb

# Connect to DuckDB and load data
con = duckdb.connect(database=":memory:", read_only=False)
con.execute(
    "CREATE TABLE data (Customer_ID INTEGER, Customer_Name VARCHAR, Age INTEGER, Gender VARCHAR, Purchase_Amount FLOAT, Purchase_Date DATE)"
)

# Read data from CSV file into DuckDB table
con.execute("COPY data FROM './data/sample_data.csv' WITH HEADER CSV")

# Remove duplicate rows based on customer ID
print("====================== Removing duplicate rows ======================")
con.execute("CREATE TABLE data_unique AS SELECT DISTINCT * FROM data")

# Handle missing values (replace with 0 for simplicity)
print("====================== Handling missing values ======================")
con.execute(
    "CREATE TABLE data_cleaned_missing AS SELECT \
             Customer_ID, Customer_Name, \
             COALESCE(Age, 0) AS Age, \
             Gender, \
             COALESCE(Purchase_Amount, 0.0) AS Purchase_Amount, \
             Purchase_Date \
             FROM data_unique"
)

# Remove outliers (e.g., age > 100 or purchase amount > 1000)
print("====================== Removing outliers ======================")
con.execute(
    "CREATE TABLE data_cleaned_outliers AS SELECT * FROM data_cleaned_missing \
             WHERE Age <= 100 AND Purchase_Amount <= 1000"
)

# Convert Gender column to binary format (0 for Female, 1 for Male)
print("====================== Converting Gender column ======================")
con.execute(
    "CREATE TABLE data_cleaned_gender AS SELECT *, \
             CASE WHEN Gender = 'Female' THEN 0 ELSE 1 END AS Gender_Binary \
             FROM data_cleaned_outliers"
)

# Split Customer_Name into First_Name and Last_Name columns
print("====================== Splitting Customer_Name ======================")
con.execute(
    "CREATE TABLE data_cleaned AS SELECT \
             Customer_ID, \
             SPLIT_PART(Customer_Name, ' ', 1) AS First_Name, \
             SPLIT_PART(Customer_Name, ' ', 2) AS Last_Name, \
             Age, Gender_Binary, Purchase_Amount, Purchase_Date \
             FROM data_cleaned_gender"
)

# Calculate total purchase amount by Gender
print(
    "====================== Calculating total purchase amount by Gender ======================"
)
total_purchase_by_gender = con.execute(
    "SELECT Gender_Binary, SUM(Purchase_Amount) AS Total_Purchase_Amount \
                                        FROM data_cleaned_gender \
                                        GROUP BY Gender_Binary"
).fetchall()
# Calculate average purchase amount by Age group
print(
    "====================== Calculating average purchase amount by Age group ======================"
)
average_purchase_by_age_group = con.execute(
    "SELECT CASE \
                                             WHEN Age BETWEEN 18 AND 30 THEN '18-30' \
                                             WHEN Age BETWEEN 31 AND 40 THEN '31-40' \
                                             WHEN Age BETWEEN 41 AND 50 THEN '41-50' \
                                             WHEN Age BETWEEN 51 AND 60 THEN '51-60' \
                                             ELSE '61-70' END AS Age_Group, \
                                             AVG(Purchase_Amount) AS Average_Purchase_Amount \
                                             FROM data_cleaned \
                                             GROUP BY Age_Group"
).fetchall()

# Print results
print("====================== Results ======================")
print("Total purchase amount by Gender:")
print(total_purchase_by_gender)
print("Average purchase amount by Age group:")
print(average_purchase_by_age_group)
