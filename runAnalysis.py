from src.config import getConfig
from src.dataIngest import fetchPriceData
from src.analytics import computeMetrics
from src.visualize import generatePlots

def main():
    cfg = getConfig()

    prices = fetchPriceData(cfg)
    results = computeMetrics(prices, cfg)
    generatePlots(prices, results, cfg)

if __name__ == "__main__":
    main()
