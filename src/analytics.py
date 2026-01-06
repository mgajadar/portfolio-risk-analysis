import numpy as np
import pandas as pd

def computeReturns(prices: pd.DataFrame) -> pd.DataFrame:
    return prices.pct_change().dropna()

def computeMetrics(prices: pd.DataFrame, cfg):
    returns = computeReturns(prices)

    meanReturns = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)
    sharpeRatio = (meanReturns - cfg.riskFreeRate) / volatility
    correlation = returns.corr()

    portfolioReturns = returns.mean(axis=1)
    cumulativeReturns = (1 + portfolioReturns).cumprod()

    maxDrawdown = (
        cumulativeReturns / cumulativeReturns.cummax() - 1
    ).min()

    return {
        "returns": returns,
        "meanReturns": meanReturns,
        "volatility": volatility,
        "sharpeRatio": sharpeRatio,
        "correlation": correlation,
        "cumulativeReturns": cumulativeReturns,
        "maxDrawdown": float(maxDrawdown)
    }
