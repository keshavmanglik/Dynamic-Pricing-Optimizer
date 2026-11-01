# Dynamic Pricing Strategy Optimizer (Prototype)

An academic prototype combining a React/Vite CSV-upload interface with Python-based
transaction-data cleaning, quality checks and exploratory analysis.

## Current implementation

- React frontend: CSV upload, dataset preview (first 10 rows), and user-defined column mapping.
- Python scripts: column-name normalisation, date parsing, duplicate removal, data-quality checks,
  category/SKU summaries, and export of a cleaned CSV.
- EDA: reproducible script generating three descriptive charts.

## Dataset

The included `scanner_data.csv` contains 131,706 records and these fields:
`Unnamed: 0`, `Date`, `Customer_ID`, `Transaction_ID`, `SKU_Category`, `SKU`, `Quantity`, `Sales_Amount`.

The data spans 02 Jan 2016 to 31 Dec 2016. It contains
22,625 unique customers, 5,242 unique SKUs and
187 SKU categories.

**Important scope limitation:** this supplied transaction dataset does not contain an explicit
unit selling-price field, competitor price, promotion flag, channel, or measured price elasticity.
`Sales_Amount / Quantity` can be explored as a transaction-value-per-unit proxy only where
quantity is positive; it must not be presented as a verified product price. This prototype
therefore does not claim to calculate validated price elasticity or automatically optimise prices.

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite (typically `http://localhost:5173`).

## Run Python data processing

From the repository root:

```bash
pip install -r requirements.txt
cd python
python main.py
```

The script expects `scanner_data.csv` in the same directory as `main.py`. For the repository's
current folder layout, copy `data/scanner_data.csv` into `python/` before running, or update the
path in `python/main.py` to `../data/scanner_data.csv`. The original script was retained with
minimal changes for transparency.

## Run EDA

```bash
python analysis/eda.py
```

The EDA script reads `data/scanner_data.csv` and saves charts under `analysis/charts/`.

## Repository structure

- `frontend/` — React/Vite source code
- `python/` — original Python data-processing scripts
- `data/` — source and cleaned datasets
- `analysis/` — EDA script and visualisations

## Academic integrity and limitations

This repository documents a prototype. The current React button labelled “Continue to Analysis”
is not connected to a working analysis service. No backend API, live price-optimisation engine,
deployment, or verified elasticity model is included. Results in the report are descriptive
statistics from the included dataset, not causal pricing recommendations.
