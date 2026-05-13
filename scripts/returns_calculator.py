# returns_calculator.py

import pandas as pd


def calculate_returns(price_data):
    """
    Calculate:
    1. Daily Returns
    2. Mean Returns
    3. Covariance Matrix
    """

    # Daily percentage returns
    daily_returns = price_data.pct_change().dropna()

    # Average return of each stock
    mean_returns = daily_returns.mean()

    # Covariance matrix
    covariance_matrix = daily_returns.cov()

    return daily_returns, mean_returns, covariance_matrix