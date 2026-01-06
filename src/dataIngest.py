import yfinance as yf
import pandas as pd

def fetchPriceData(cfg) -> pd.DataFrame:
    data = yf.download(
        cfg.tickers,
        start=cfg.startDate,
        end=cfg.endDate,
        progress=False
    )["Adj Close"]

    data = data.dropna()
    return data
