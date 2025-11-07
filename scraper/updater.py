import os
import pandas as pd

def update_csv(df, filename="data/prices.csv"):
    """
    Append new data to CSV. Create file if it doesn't exist.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if os.path.exists(filename):
        existing = pd.read_csv(filename, parse_dates=["Date"])
        df = pd.concat([existing, df]).drop_duplicates(subset=["Date", "Ticker"])
    df.to_csv(filename, index=False)
    print(f"Updated {filename} with {len(df)} rows")
