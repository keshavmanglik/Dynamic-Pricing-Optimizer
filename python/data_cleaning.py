import pandas as pd


def clean_data(data):

    # Standardize column names
    data.columns = data.columns.str.strip().str.lower()

    # Remove unnecessary index column if present
    if "unnamed: 0" in data.columns:
        data = data.drop(columns=["unnamed: 0"])

    # Convert date into proper date format
    data["date"] = pd.to_datetime(
        data["date"],
        dayfirst=True,
        errors="coerce"
    )

    print("Data cleaning completed.")

    return data 