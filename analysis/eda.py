"""
Exploratory data analysis for the Dynamic Pricing Strategy Optimizer prototype.
Run from the project root: python analysis/eda.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "scanner_data.csv"
OUT = ROOT / "analysis" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)
df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly = df.groupby("Month")["Sales_Amount"].sum()
monthly.plot(kind="bar", figsize=(10, 5), title="Monthly Recorded Sales Amount")
plt.ylabel("Sales_Amount (dataset units)")
plt.tight_layout()
plt.savefig(OUT / "monthly_sales.png", dpi=160)
plt.close()

df["SKU_Category"].value_counts().head(10).sort_values().plot(
    kind="barh", figsize=(10, 5), title="Top 10 SKU Categories by Record Count"
)
plt.xlabel("Number of records")
plt.tight_layout()
plt.savefig(OUT / "top_categories.png", dpi=160)
plt.close()

pd.cut(df["Quantity"], bins=[0, 1, 2, 5, 10, 25, 50, 500]).value_counts().sort_index().plot(
    kind="bar", figsize=(10, 5), title="Quantity Distribution"
)
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig(OUT / "quantity_distribution.png", dpi=160)
plt.close()

print("Rows:", len(df))
print("Columns:", list(df.columns))
print("Missing cells:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
print("Unique customers:", df["Customer_ID"].nunique())
print("Unique SKUs:", df["SKU"].nunique())
print("Charts saved to:", OUT)
