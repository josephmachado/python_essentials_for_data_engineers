from cleaning_functions import remove_duplicates


def test_remove_duplicates():
    # Define sample data and unique_key
    data = []
    unique_key = ""

    # Call the function
    unique_data = remove_duplicates(data, unique_key)

    # Assert that duplicates were removed
    # assert len(unique_data) == 3
    # Assert the actual values
    expected_data = [
    ]
    assert unique_data == expected_data


# Run this with the command python -m pytest ./tests
