def analyze_data(data):

    print("\nData types:")
    print(data.dtypes)

    print("\nFirst 5 rows of cleaned data:")
    print(data.head())

    print("\nProducts by category:")
    print(
        data["sku_category"]
        .value_counts()
        .head(10)
    )

    print("\nTop SKUs by number of records:")
    print(
        data["sku"]
        .value_counts()
        .head(10)
    )

    print("\nUnique values:")
    print(data.nunique())

    return data 