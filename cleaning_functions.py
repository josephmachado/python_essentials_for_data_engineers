# Simple function to remove duplicates


def remove_duplicates(data, unique_key):
    data_unique = []
    unique_key_set = set()

    for row in data:
        if row[unique_key] not in unique_key_set:
            data_unique.append(row)
            unique_key_set.add(row[unique_key])
    else:
        print(f"duplicate customer id")

    return data_unique
