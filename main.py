# main.py

from scripts.data_fetcher import fetch_stock_data

from scripts.returns_calculator import (
    calculate_returns
)

from scripts.risk_calculator import (
    portfolio_return,
    portfolio_variance,
    portfolio_volatility,
    sharpe_ratio
)

from scripts.optimizer import (
    generate_random_portfolios,
    maximize_sharpe_ratio,
    minimize_volatility
)

from scripts.visualization import (
    plot_efficient_frontier,
    plot_risk_return,
    plot_allocation
)

import numpy as np


def main():

    print("\n===== Portfolio Risk Analyzer =====\n")

    # -----------------------------------
    # User Input
    # -----------------------------------
    stocks = input(
        "Enter stock symbols separated by comma: "
    ).upper().split(",")

    stocks = [
        stock.strip()
        for stock in stocks
    ]

    print("\nFetching stock data...\n")

    # -----------------------------------
    # Fetch Stock Data
    # -----------------------------------
    stock_data = fetch_stock_data(stocks)

    if stock_data.empty:

        print("No data found.")
        return

    # -----------------------------------
    # Calculate Returns
    # -----------------------------------
    daily_returns, mean_returns, covariance_matrix = (
        calculate_returns(stock_data)
    )

    # -----------------------------------
    # Equal Portfolio Weights
    # -----------------------------------
    num_stocks = len(stocks)

    weights = np.array(
        [1 / num_stocks] * num_stocks
    )

    # -----------------------------------
    # Portfolio Metrics
    # -----------------------------------
    expected_return = portfolio_return(
        weights,
        mean_returns
    )

    variance = portfolio_variance(
        weights,
        covariance_matrix
    )

    volatility = portfolio_volatility(
        weights,
        covariance_matrix
    )

    sharpe = sharpe_ratio(
        expected_return,
        volatility
    )

    # -----------------------------------
    # Display Portfolio Summary
    # -----------------------------------
    print("========== Portfolio Summary ==========\n")

    print("Stocks:", stocks)

    print("\nWeights:")

    for stock, weight in zip(stocks, weights):

        print(
            f"{stock}: {round(weight * 100, 2)}%"
        )

    print(
        "\nExpected Annual Return:",
        round(expected_return * 252 * 100, 2),
        "%"
    )

    print(
        "Portfolio Variance:",
        round(variance, 6)
    )

    print(
        "Portfolio Volatility (Risk):",
        round(volatility * np.sqrt(252) * 100, 2),
        "%"
    )

    print(
        "Sharpe Ratio:",
        round(sharpe, 4)
    )

    print("\n=======================================\n")

    # -----------------------------------
    # Generate Efficient Frontier
    # -----------------------------------
    results = generate_random_portfolios(
        mean_returns,
        covariance_matrix
    )

    # -----------------------------------
    # Optimize Portfolios
    # -----------------------------------
    max_sharpe_portfolio = maximize_sharpe_ratio(
        mean_returns,
        covariance_matrix
    )

    min_volatility_portfolio = minimize_volatility(
        mean_returns,
        covariance_matrix
    )

    # -----------------------------------
    # Best Portfolio Indexes
    # -----------------------------------
    max_sharpe_idx = np.argmax(
        results["sharpe_ratio"]
    )

    min_vol_idx = np.argmin(
        results["volatility"]
    )

    # -----------------------------------
    # Visualization
    # -----------------------------------

    # Efficient Frontier
    plot_efficient_frontier(
        results,
        max_sharpe_idx,
        min_vol_idx
    )

    # Risk vs Return Scatter Plot
    plot_risk_return(results)

    # Allocation Pie Chart
    best_weights = results["weights"][
        max_sharpe_idx
    ]

    plot_allocation(
        best_weights,
        stocks
    )


if __name__ == "__main__":
    main()