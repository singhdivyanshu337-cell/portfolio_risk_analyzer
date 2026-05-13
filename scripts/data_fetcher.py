# data_fetcher.py

import yfinance as yf
import pandas as pd


def fetch_stock_data(tickers, start="2024-01-01", end=None):
    """
    Fetch closing prices for multiple stocks

    Parameters:
    tickers : list
        List of stock symbols
    start : str
        Start date (YYYY-MM-DD)
    end : str
        End date (YYYY-MM-DD)

    Returns:
    DataFrame containing closing prices
    """

    # Download stock data
    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True
    )

    # Extract only Close prices
    close_prices = data["Close"]

    return close_prices


# Example usage
if __name__ == "__main__":

    stocks = ["AAPL", "MSFT", "GOOGL", "TSLA"]

    prices = fetch_stock_data(stocks)

    print("\nClosing Prices:\n")
    print(prices.tail())