def remove_duplicates(data):

    print("\nDuplicate rows before cleaning:")
    print(data.duplicated().sum())

    data = data.drop_duplicates()

    print("Duplicate rows after cleaning:")
    print(data.duplicated().sum())

    return data