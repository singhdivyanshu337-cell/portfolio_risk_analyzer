# optimizer.py

import numpy as np
from scipy.optimize import minimize


# -----------------------------------
# Portfolio Performance
# -----------------------------------
def portfolio_performance(
    weights,
    mean_returns,
    cov_matrix,
    risk_free_rate=0.05
):

    # Annual Return
    portfolio_return = np.sum(
        mean_returns * weights
    ) * 252

    # Annual Volatility
    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(cov_matrix * 252, weights)
        )
    )

    # Sharpe Ratio
    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_volatility

    return (
        portfolio_return,
        portfolio_volatility,
        sharpe_ratio
    )


# -----------------------------------
# Generate Efficient Frontier
# -----------------------------------
def generate_random_portfolios(
    mean_returns,
    cov_matrix,
    risk_free_rate=0.05,
    num_portfolios=5000
):

    results = {
        "returns": [],
        "volatility": [],
        "sharpe_ratio": [],
        "weights": []
    }

    num_assets = len(mean_returns)

    for _ in range(num_portfolios):

        # Random weights
        weights = np.random.random(num_assets)

        # Normalize
        weights /= np.sum(weights)

        # Metrics
        portfolio_return, portfolio_volatility, sharpe = (
            portfolio_performance(
                weights,
                mean_returns,
                cov_matrix,
                risk_free_rate
            )
        )

        results["returns"].append(
            portfolio_return
        )

        results["volatility"].append(
            portfolio_volatility
        )

        results["sharpe_ratio"].append(
            sharpe
        )

        results["weights"].append(weights)

    # Convert to numpy arrays
    results["returns"] = np.array(
        results["returns"]
    )

    results["volatility"] = np.array(
        results["volatility"]
    )

    results["sharpe_ratio"] = np.array(
        results["sharpe_ratio"]
    )

    return results


# -----------------------------------
# Max Sharpe Ratio Optimization
# -----------------------------------
def maximize_sharpe_ratio(
    mean_returns,
    cov_matrix,
    risk_free_rate=0.05
):

    num_assets = len(mean_returns)

    # Initial equal weights
    initial_weights = np.ones(num_assets) / num_assets

    # Constraint
    constraints = ({
        "type": "eq",
        "fun": lambda x: np.sum(x) - 1
    })

    # Bounds
    bounds = tuple(
        (0, 1)
        for asset in range(num_assets)
    )

    # Negative Sharpe Ratio
    def negative_sharpe(weights):

        return -portfolio_performance(
            weights,
            mean_returns,
            cov_matrix,
            risk_free_rate
        )[2]

    optimized = minimize(
        negative_sharpe,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return optimized


# -----------------------------------
# Minimum Volatility Optimization
# -----------------------------------
def minimize_volatility(
    mean_returns,
    cov_matrix
):

    num_assets = len(mean_returns)

    # Initial equal weights
    initial_weights = np.ones(num_assets) / num_assets

    # Constraint
    constraints = ({
        "type": "eq",
        "fun": lambda x: np.sum(x) - 1
    })

    # Bounds
    bounds = tuple(
        (0, 1)
        for asset in range(num_assets)
    )

    # Portfolio volatility
    def portfolio_volatility(weights):

        return portfolio_performance(
            weights,
            mean_returns,
            cov_matrix
        )[1]

    optimized = minimize(
        portfolio_volatility,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return optimized