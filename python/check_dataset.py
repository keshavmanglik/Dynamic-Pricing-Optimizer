import pandas as pd

data = pd.read_csv("scanner_data.csv")

print(data.head())
print(data.shape)
print(data.columns)
print(data.info())