import yfinance as yf

def fetch_data(ticker):
    """
    Fetch daily stock data for a ticker using yfinance.
    Returns a pandas DataFrame.
    """
    data = yf.download(ticker, period="5d", interval="1d")  # last 5 days
    if data.empty:
        print(f"No data for {ticker}")
    return data
