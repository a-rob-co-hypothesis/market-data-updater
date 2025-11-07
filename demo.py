import yaml
import pandas as pd
from scraper import fetcher, parser, updater, utils

# Load configuration
with open("config/config.yml") as f:
    config = yaml.safe_load(f)

tickers = config.get("tickers", [])
storage = config.get("storage", "csv")

for ticker in tickers:
    utils.log(f"Fetching data for {ticker}")
    df = fetcher.fetch_data(ticker)
    if df.empty:
        continue
    df_norm = parser.normalize_data(df, ticker)
    if storage == "csv":
        updater.update_csv(df_norm)
