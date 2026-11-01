
import pandas as pd


def check_data_quality(data):

    print("\nMissing values:")
    print(data.isnull().sum())

    print("\nDuplicate rows:")
    print(data.duplicated().sum())

    print("\nNegative values:")
    print(data.select_dtypes(include="number").lt(0).sum())

    print("\nZero values:")
    print((data.select_dtypes(include="number") == 0).sum())

    print("\nData types:")
    print(data.dtypes)

    print("\nDataset shape:")
    print(data.shape)

    print("\nData quality check completed.")

    return data 