import csv
import os
import sqlite3


def del_existing_db(db_path):
    # Delete file if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"{db_path} has been deleted.")
    else:
        print(f"{db_path} does not exist.")


del_existing_db("tpch.db")
del_existing_db("duckdb.db")

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("tpch.db")
cursor = conn.cursor()

# Create Customer table
cursor.execute("DROP TABLE IF EXISTS Customer")
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER PRIMARY KEY,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    datetime_created TEXT,
    datetime_updated TEXT
)
"""
)


# Function to read CSV and insert data into the table
def insert_data_from_csv(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                """
                INSERT INTO Customer (customer_id, zipcode, city, state_code, datetime_created, datetime_updated)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    row["customer_id"],
                    row["zipcode"],
                    row["city"],
                    row["state_code"],
                    row["datetime_created"],
                    row["datetime_updated"],
                ),
            )
    conn.commit()


# Insert data from CSV file
insert_data_from_csv("./data/customers.csv")

# Close the database connection
conn.close()

print("Data inserted successfully!")


import duckdb

# Connect to the DuckDB database (or create it if it doesn't exist)
duckdb_conn = duckdb.connect("duckdb.db")

# Create the Customer table in DuckDB
duckdb_conn.execute("DROP TABLE IF EXISTS Customer")
duckdb_conn.execute(
    """
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    datetime_created TIMESTAMP,
    datetime_updated TIMESTAMP
)
"""
)

duckdb_conn.execute("DROP TABLE IF EXISTS WeatherData")
duckdb_conn.execute(
    """
CREATE TABLE IF NOT EXISTS WeatherData (
    id TEXT,
    date TEXT,
    element TEXT,
    value INTEGER,
    m_flag TEXT,
    q_flag TEXT,
    s_flag TEXT,
    obs_time TEXT
)
"""
)

duckdb_conn.execute("DROP TABLE IF EXISTS Exchanges")
duckdb_conn.execute(
    """
CREATE TABLE IF NOT EXISTS Exchanges (
    id TEXT,
    name TEXT,
    rank INTEGER,
    percentTotalVolume FLOAT,
    volumeUsd FLOAT,
    tradingPairs TEXT,
    socket BOOLEAN,
    exchangeUrl TEXT,
    updated BIGINT 
)
"""
)

# Commit and close the connection
duckdb_conn.commit()
duckdb_conn.close()

print("Customer table created successfully!")

import csv
import datetime
import random


# Generate random customer names
def generate_name():
    first_names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
    ]
    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
    ]
    return random.choice(first_names) + " " + random.choice(last_names)


# Generate random age between 18 and 70
def generate_age():
    return random.randint(18, 70)


# Generate random gender
def generate_gender():
    return random.choice(["Male", "Female"])


# Generate random purchase amount between 10 and 1000
def generate_purchase_amount():
    return round(random.uniform(10, 1000), 2)


# Generate random purchase date within the last year
def generate_purchase_date():
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=365)
    random_date = start_date + datetime.timedelta(days=random.randint(0, 365))
    return random_date.strftime("%Y-%m-%d")


# Generate CSV data
with open("./data/sample_data.csv", "w", newline="") as csvfile:
    fieldnames = [
        "Customer_ID",
        "Customer_Name",
        "Age",
        "Gender",
        "Purchase_Amount",
        "Purchase_Date",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(100):
        writer.writerow(
            {
                "Customer_ID": i + 1,
                "Customer_Name": generate_name(),
                "Age": generate_age(),
                "Gender": generate_gender(),
                "Purchase_Amount": generate_purchase_amount(),
                "Purchase_Date": generate_purchase_date(),
            }
        )

print("CSV file generated successfully!")
