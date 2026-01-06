import matplotlib.pyplot as plt

def generatePlots(prices, results, cfg):
    # cumulative returns
    plt.figure()
    results["cumulativeReturns"].plot()
    plt.title("Portfolio Cumulative Returns")
    plt.ylabel("Growth of $1")
    plt.savefig(cfg.outputDir / "portfolio_cumulative_returns.png")
    plt.close()

    # volatility vs return
    plt.figure()
    plt.scatter(
        results["volatility"],
        results["meanReturns"]
    )

    for ticker in results["meanReturns"].index:
        plt.annotate(
            ticker,
            (results["volatility"][ticker], results["meanReturns"][ticker])
        )

    plt.xlabel("Volatility (Annualized)")
    plt.ylabel("Expected Return (Annualized)")
    plt.title("Risk vs Return")
    plt.savefig(cfg.outputDir / "risk_return_scatter.png")
    plt.close()

    # correlation heatmap
    plt.figure()
    plt.imshow(results["correlation"])
    plt.colorbar()
    plt.xticks(range(len(prices.columns)), prices.columns, rotation=45)
    plt.yticks(range(len(prices.columns)), prices.columns)
    plt.title("Asset Correlation Matrix")
    plt.savefig(cfg.outputDir / "correlation_matrix.png")
    plt.close()
