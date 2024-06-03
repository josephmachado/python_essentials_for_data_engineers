import polars as pl
from cuallee import Check, CheckLevel

# Read CSV file into Polars DataFrame
df = pl.read_csv("./data/sample_data.csv")

# Question: Check for Nulls on column Id and that Customer_ID column is unique
# check docs at https://canimus.github.io/cuallee/polars/

check = Check(CheckLevel.ERROR, "Completeness")
validation_results_df = (
    check.is_complete("Customer_ID").is_unique("Customer_ID").validate(df)
)
print(validation_results_df)

results = validation_results_df["status"].to_list()
assert "FAIL" not in results == True
