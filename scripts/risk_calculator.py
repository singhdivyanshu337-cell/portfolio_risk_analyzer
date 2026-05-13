# risk_calculator.py

import numpy as np


def portfolio_return(weights, mean_returns):
    """
    Calculate portfolio expected return

    Formula:
    Return = wᵀ μ
    """

    # Annual portfolio return
    return np.sum(mean_returns * weights) * 252


def portfolio_variance(weights, covariance_matrix):
    """
    Calculate portfolio variance

    Formula:
    Variance = wᵀ Σ w
    """

    # Annual covariance matrix
    covariance_matrix = covariance_matrix * 252

    return np.dot(
        weights.T,
        np.dot(covariance_matrix, weights)
    )


def portfolio_volatility(weights, covariance_matrix):
    """
    Calculate portfolio volatility (risk)

    Formula:
    Risk = √(wᵀ Σ w)
    """

    variance = portfolio_variance(
        weights,
        covariance_matrix
    )

    return np.sqrt(variance)


def sharpe_ratio(portfolio_return_value,
                 portfolio_volatility_value,
                 risk_free_rate=0.01):
    """
    Calculate Sharpe Ratio

    Formula:
    Sharpe Ratio =
    (Portfolio Return - Risk Free Rate)
    / Portfolio Volatility
    """

    return (
        portfolio_return_value - risk_free_rate
    ) / portfolio_volatility_value


def portfolio_performance(weights,
                          mean_returns,
                          covariance_matrix):
    """
    Calculate complete portfolio performance
    """

    # Portfolio return
    port_return = portfolio_return(
        weights,
        mean_returns
    )

    # Portfolio volatility
    volatility = portfolio_volatility(
        weights,
        covariance_matrix
    )

    # Sharpe ratio
    sharpe = sharpe_ratio(
        port_return,
        volatility
    )

    return (
        port_return,
        volatility,
        sharpe
    )


# Example usage
if __name__ == "__main__":

    # Example weights
    weights = np.array([0.4, 0.3, 0.3])

    # Example mean returns
    mean_returns = np.array([
        0.12,
        0.10,
        0.15
    ])

    # Example covariance matrix
    covariance_matrix = np.array([
        [0.005, -0.010, 0.004],
        [-0.010, 0.040, -0.002],
        [0.004, -0.002, 0.023]
    ])

    # Portfolio calculations
    port_return, volatility, sharpe = (
        portfolio_performance(
            weights,
            mean_returns,
            covariance_matrix
        )
    )

    # Output
    print(
        "Portfolio Return:",
        round(port_return, 4)
    )

    print(
        "Portfolio Volatility:",
        round(volatility, 4)
    )

    print(
        "Sharpe Ratio:",
        round(sharpe, 4)
    )