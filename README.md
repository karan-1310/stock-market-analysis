# Stock Market Data Analysis

**Role targeting:** Market Analyst / Equity Research / Data Analyst

## Objective
Fetch historical stock prices, clean/transform the data, compute technical indicators (moving averages, daily returns, volatility), analyze correlations, and visualize trends for actionable insights.

## What this shows a recruiter
- Data sourcing via API (`yfinance`) with robust fallback to local sample data
- Feature engineering (rolling windows, returns, volatility)
- Exploratory analysis and clean visualizations (matplotlib)
- Clear narrative in notebook + reproducible script

## How to run
```bash
pip install -r requirements.txt
# Option 1: run the notebook
jupyter lab  # or jupyter notebook
# open stock_analysis.ipynb and run all cells
# Option 2: run the script
python stock_analysis.py
```

## Files
- `stock_analysis.ipynb` (if created) and `stock_analysis.py`
- `data/AAPL_MSFT_sample.csv` (for offline runs)
- `requirements.txt`

## Resume bullets
- Built an end-to-end stock analytics pipeline using Python (Pandas/matplotlib) to compute returns, volatility, and cross-asset correlations; documented insights with clear visuals.
- Implemented robust data ingestion with API fallback and caching for reproducibility.
