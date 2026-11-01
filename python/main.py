import pandas as pd

from data_cleaning import clean_data
from duplicate import remove_duplicates
from data_quality import check_data_quality
from data_analysis import analyze_data


# 1. Load original dataset
data = pd.read_csv("../data/scanner_data.csv")

print("Original dataset loaded.")


# 2. Clean the data
data = clean_data(data)


# 3. Remove duplicate rows
data = remove_duplicates(data)


# 4. Check data quality
data = check_data_quality(data)


# 5. Analyze the data
data = analyze_data(data)


# 6. Save final processed dataset
data.to_csv("../data/cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
print("File: cleaned_data.csv")