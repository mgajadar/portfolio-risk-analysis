from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Config:
    tickers: list
    startDate: str
    endDate: str
    riskFreeRate: float
    outputDir: Path

def getConfig() -> Config:
    outputDir = Path("outputs")
    outputDir.mkdir(exist_ok=True)

    return Config(
        tickers=["AAPL", "MSFT", "GOOGL", "AMZN", "SPY"],
        startDate="2019-01-01",
        endDate="2024-01-01",
        riskFreeRate=0.02,
        outputDir=outputDir
    )
