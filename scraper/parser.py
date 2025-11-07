def normalize_data(df, ticker):
    """
    Normalize DataFrame by adding ticker column and selecting relevant fields.
    """
    df = df.copy()
    df["Ticker"] = ticker
    df = df.reset_index()  # reset index to get Date as a column
    return df[["Date", "Ticker", "Open", "High", "Low", "Close", "Volume"]]
