import pytest
from sqlframe.duckdb import DuckDBSession
from freezegun import freeze_time

from sqlframe.duckdb import functions as F



def transform(orders_df, customer_df, as_of=None):
    as_of_col = F.current_date() if as_of is None else F.lit(as_of).cast("date")

    # 1. Left join orders -> customer
    enriched_orders_df = orders_df.join(
        customer_df,
        orders_df["customer_id"] == customer_df["id"],
        how="left",
    )

    # 2. Age from date_of_birth vs as_of (full years by year difference)
    enriched_orders_df = enriched_orders_df.withColumn(
        "age",
        (F.year(as_of_col) - F.year(F.to_date("date_of_birth"))).cast("int"),
    )

    # 3. Age bucket
    enriched_orders_df = enriched_orders_df.withColumn(
        "age_bucket",
        F.when(F.col("age") < 18, "lt18")
         .when(F.col("age") <= 30, "18-30")
         .when(F.col("age") <= 50, "31-50")
         .when(F.col("age") <= 70, "51-70")
         .otherwise("70+"),
    )

    return enriched_orders_df
    
@pytest.fixture(scope="session")
def spark():
    return DuckDBSession()


def test_age_bucket(spark):
    orders_df = spark.createDataFrame(
        [
            (1, 101),
            (2, 102),
            (3, 103),
            (4, 104),
            (5, 105),
        ],
        ["order_id", "customer_id"],
    )
    customer_df = spark.createDataFrame(
        [
            (101, "2010-01-01"),  # age 15 -> lt18
            (102, "2000-01-01"),  # age 25 -> 18-30
            (103, "1985-01-01"),  # age 40 -> 31-50
            (104, "1965-01-01"),  # age 60 -> 51-70
            (105, "1940-01-01"),  # age 85 -> 70+
        ],
        ["id", "date_of_birth"],
    )

    rows = transform(orders_df, customer_df, as_of="2025-01-01").collect()
    got = {r["customer_id"]: (r["age"], r["age_bucket"]) for r in rows}

    assert got == {
        101: (15, "lt18"),
        102: (25, "18-30"),
        103: (40, "31-50"),
        104: (60, "51-70"),
        105: (85, "70+"),
    }