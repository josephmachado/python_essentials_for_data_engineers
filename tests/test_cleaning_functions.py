from cleaning_functions import remove_duplicates


def test_remove_duplicates():
    # Define sample data and unique key
    data = [
        {"Customer_ID": 1, "Name": "Alice"},
        {"Customer_ID": 2, "Name": "Bob"},
        {"Customer_ID": 1, "Name": "Alice"},  # Duplicate
        {"Customer_ID": 3, "Name": "Charlie"},
        {"Customer_ID": 2, "Name": "Bob"},  # Duplicate
    ]
    unique_key = "Customer_ID"

    # Call the function
    unique_data = remove_duplicates(data, unique_key)

    # Assert that duplicates were removed
    assert len(unique_data) == 3


# Run this with python -m pytest ./tests
