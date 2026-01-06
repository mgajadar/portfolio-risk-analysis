# Portfolio Risk & Return Analysis

This project analyzes the risk and return characteristics of a simple equity portfolio using historical market data.

The focus is on understanding how assets behave individually and together, rather than on forecasting prices.

---

## What this looks at

- historical returns and volatility
- risk–return tradeoffs across assets
- correlations and diversification effects
- portfolio-level performance and drawdowns

---

## Data

Daily adjusted close prices are pulled using `yfinance` for a small set of large-cap equities and an index ETF.

Returns are computed from price data and annualized using standard market conventions.

---

## Analysis

The pipeline:
- computes daily and annualized returns
- estimates volatility and Sharpe ratios
- evaluates correlations between assets
- tracks cumulative portfolio performance
- calculates maximum drawdown

Results are saved as plots for quick review.

---

## Running the analysis

```bash
python -m venv .venv
pip install -r requirements.txt
python runAnalysis.py
