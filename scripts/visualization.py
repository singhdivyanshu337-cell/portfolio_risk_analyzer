# visualization.py

import matplotlib.pyplot as plt


# -----------------------------
# Efficient Frontier
# -----------------------------
def plot_efficient_frontier(
    results,
    max_sharpe_idx,
    min_vol_idx
):

    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(
        results["volatility"],
        results["returns"],
        c=results["sharpe_ratio"],
        cmap="viridis",
        marker="o"
    )

    fig.colorbar(
        scatter,
        label="Sharpe Ratio"
    )

    # Maximum Sharpe Ratio Portfolio
    ax.scatter(
        results["volatility"][max_sharpe_idx],
        results["returns"][max_sharpe_idx],
        color="red",
        marker="*",
        s=300,
        label="Max Sharpe Ratio"
    )

    # Minimum Volatility Portfolio
    ax.scatter(
        results["volatility"][min_vol_idx],
        results["returns"][min_vol_idx],
        color="blue",
        marker="*",
        s=300,
        label="Minimum Volatility"
    )

    ax.set_title("Efficient Frontier")

    ax.set_xlabel("Volatility (Risk)")

    ax.set_ylabel("Expected Return")

    ax.legend()

    ax.grid(True)

    return fig


# -----------------------------
# Risk vs Return Scatter Plot
# -----------------------------
def plot_risk_return(results):

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(
        results["volatility"],
        results["returns"],
        alpha=0.6
    )

    ax.set_title("Risk vs Return")

    ax.set_xlabel("Risk (Volatility)")

    ax.set_ylabel("Return")

    ax.grid(True)

    return fig


# -----------------------------
# Portfolio Allocation Pie Chart
# -----------------------------
def plot_allocation(
    weights,
    stock_names
):

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.pie(
        weights,
        labels=stock_names,
        autopct="%1.1f%%",
        startangle=140
    )

    ax.set_title("Portfolio Allocation")

    return fig