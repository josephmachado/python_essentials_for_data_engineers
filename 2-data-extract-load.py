# Extract: Process to pull data from Source system
# Load: Process to write data to a destination system

# Common upstream & downstream systems
# OLTP Databases: Postgres, MySQL, sqlite3, etc
# OLAP Databases: Snowflake, BigQuery, Clickhouse, DuckDB, etc
# Cloud data storage: AWS S3, GCP Cloud Store, Minio, etc
# Queue systems: Kafka, Redpanda, etc
# API
# Local disk: csv, excel, json, xml files
# SFTP\FTP server

## Databases: When reading or writing to a database we use a database driver. Database driver's are libraries that we can use to read or write to a database.
## Question: Read data from a sqlite3 database and write to a DuckDB database (note: DuckDB has tools to do this easily, this code is for demo)
print("======== sqlite3 -> DuckDB ===============")
import sqlite3  # we import the sqlite3 database driver

# Connect to the SQLite database
sqlite_conn = sqlite3.connect(
    "tpch.db"
)  # Typically this will involve a connection string, sqlite3 db is stored as a file

# Fetch data from the SQLite Customer table using conn.execute
customers = sqlite_conn.execute(
    "SELECT * FROM Customer"
).fetchall()  # Fetch data from the SQLite Customer table

import duckdb  # duckdb database driver

duckdb_conn = duckdb.connect("duckdb.db")  # Duckdb connection string
# Insert data into the DuckDB Customer table
insert_query = f"""
INSERT INTO Customer (customer_id, zipcode, city, state_code, datetime_created, datetime_updated)
VALUES (?, ?, ?, ?, ?, ?)
"""  # Insert into query

duckdb_conn.executemany(insert_query, customers)

# Commit and close the connections
sqlite_conn.commit()
duckdb_conn.commit()
sqlite_conn.close()
duckdb_conn.close()

print("Data transferred successfully!")

## Cloud storage
## Question: Read data from the S3 location given below and write the data to a DuckDB database
## Data source: https://docs.opendata.aws/noaa-ghcn-pds/readme.html␛
print("======== Weather S3 -> DuckDB ===============")
import csv
import gzip
from io import StringIO

import boto3
import duckdb
from botocore import UNSIGNED
from botocore.client import Config

# AWS S3 bucket and file details
bucket_name = "noaa-ghcn-pds"
file_key = "csv.gz/by_station/ASN00002022.csv.gz"
# Create a boto3 client with anonymous access
s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))

# Download the CSV file from S3
response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
compressed_data = response["Body"].read()

# Decompress the gzip data
csv_data = gzip.decompress(compressed_data).decode("utf-8")

# Read the CSV file using csv.reader
csv_reader = csv.reader(StringIO(csv_data))
data = list(csv_reader)
# Connect to the DuckDB database (assume WeatherData table exists)
duckdb_conn = duckdb.connect("duckdb.db")

# Insert data into the DuckDB WeatherData table
insert_query = """
INSERT INTO WeatherData (id, date, element, value, m_flag, q_flag, s_flag, obs_time)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

duckdb_conn.executemany(insert_query, data[:100000])

# Commit and close the connection
duckdb_conn.commit()
duckdb_conn.close()

print("Data transferred successfully!")

## API
## Question: Read data from CoinCap API given below and write the data to a DuckDB database
print("======== API -> DuckDB ===============")
import duckdb
import requests

# Define the API endpoint
url = "https://api.coincap.io/v2/exchanges"

# Fetch data from the CoinCap API
response = requests.get(url)
data = response.json()["data"]

# Connect to the DuckDB database
duckdb_conn = duckdb.connect("duckdb.db")

# Insert data into the DuckDB Exchanges table
insert_query = """
INSERT INTO Exchanges (id, name, rank, percentTotalVolume, volumeUsd, tradingPairs, socket, exchangeUrl, updated)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
# Prepare data for insertion
insert_data = [
    (
        exchange["exchangeId"],
        exchange["name"],
        int(exchange["rank"]),
        (
            float(exchange["percentTotalVolume"])
            if exchange["percentTotalVolume"]
            else None
        ),
        float(exchange["volumeUsd"]) if exchange["volumeUsd"] else None,
        exchange["tradingPairs"],
        exchange["socket"],
        exchange["exchangeUrl"],
        int(exchange["updated"]),
    )
    for exchange in data
]

duckdb_conn.executemany(insert_query, insert_data)

# Commit and close the connection
duckdb_conn.commit()
duckdb_conn.close()

print("Data transferred successfully!")

## Local disk
## Question: Read a csv file from local disk and write it to a database
print("======== Local file -> Print ===============")
import csv

data_location = "./data/customers.csv"
with open(data_location, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        print(row)
