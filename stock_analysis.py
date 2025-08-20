import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Optional import: if yfinance not installed or offline, script falls back to sample CSV
def fetch_data(tickers=("AAPL","MSFT"), period="1y"):
    try:
        import yfinance as yf
        data = {}
        for t in tickers:
            df = yf.download(t, period=period, progress=False)
            df["Ticker"] = t
            data[t] = df
        out = pd.concat(data.values(), axis=0)
        out.index.name = "Date"
        return out.reset_index()
    except Exception as e:
        print("Falling back to local sample data:", e)
        sample_path = os.path.join("data", "AAPL_MSFT_sample.csv")
        return pd.read_csv(sample_path, parse_dates=["Date"])

def compute_indicators(df):
    # pivot by ticker
    close = df.pivot(index="Date", columns="Ticker", values="Close").sort_index()
    # daily returns
    returns = close.pct_change().dropna()
    # moving averages and volatility
    ma_20 = close.rolling(20).mean()
    ma_50 = close.rolling(50).mean()
    vol_20 = returns.rolling(20).std() * np.sqrt(252)
    corr = returns.rolling(60).corr().dropna()
    return close, returns, ma_20, ma_50, vol_20, corr

def plots(close, returns, ma20, ma50, vol20):
    import matplotlib.pyplot as plt
    # Price + MAs
    ax = close.plot(figsize=(10,5), title="Close Price")
    ma20.plot(ax=ax)
    ma50.plot(ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.tight_layout()
    plt.savefig("fig_prices.png", dpi=150)
    plt.close()
    # Volatility
    ax = vol20.plot(figsize=(10,5), title="Rolling Volatility (20d, annualized)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")
    plt.tight_layout()
    plt.savefig("fig_volatility.png", dpi=150)
    plt.close()
    # Returns
    ax = returns.cumsum().plot(figsize=(10,5), title="Cumulative Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Return")
    plt.tight_layout()
    plt.savefig("fig_cum_returns.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    df = fetch_data()
    close, returns, ma20, ma50, vol20, corr = compute_indicators(df)
    plots(close, returns, ma20, ma50, vol20)
    # Basic insights
    last = close.iloc[-1]
    print("\nLatest close prices:")
    print(last.to_string())
    print("\nReturn correlations (60d rolling last value):")
    try:
        last_corr = returns.rolling(60).corr().dropna().groupby(level=1).tail(1)
        print(last_corr)
    except Exception as e:
        print("Correlation calc warning:", e)
