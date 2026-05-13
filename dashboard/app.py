# -----------------------------------
# IMPORTS
# -----------------------------------
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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


# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Portfolio Risk Analyzer",
    page_icon="📈",
    layout="wide"
)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>

/* Main App */
.main {
    background-color: #0E1117;
    color: white;
}

/* Padding */
.block-container {
    padding-top: 2rem;
}

/* Headings */
h1, h2, h3 {
    color: white;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #1f2937, #111827);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #374151;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* Metric Label */
[data-testid="stMetricLabel"] {
    color: #9CA3AF !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Metric Value */
[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 42px !important;
    font-weight: 700 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------
st.title("📊 Portfolio Risk Analyzer")

st.caption(
    "Professional Portfolio Optimization & Risk Analytics Dashboard"
)

st.markdown("---")


# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("⚙ Portfolio Settings")

stock_input = st.sidebar.text_input(
    "Enter Stock Symbols",
    "AAPL,MSFT,GOOGL"
)

risk_free_rate = st.sidebar.slider(
    "Risk Free Rate",
    0.0,
    0.15,
    0.05
)

num_portfolios = st.sidebar.slider(
    "Number of Portfolios",
    1000,
    10000,
    5000
)

analyze_button = st.sidebar.button(
    "🚀 Analyze Portfolio"
)


# -----------------------------------
# STOCK LIST
# -----------------------------------
stocks = [
    stock.strip().upper()
    for stock in stock_input.split(",")
]


# -----------------------------------
# ANALYSIS
# -----------------------------------
if analyze_button:

    with st.spinner("Fetching stock market data..."):

        stock_data = fetch_stock_data(stocks)

    if stock_data.empty:

        st.error("No stock data found.")

    else:

        # -----------------------------------
        # RETURNS CALCULATION
        # -----------------------------------
        daily_returns, mean_returns, covariance_matrix = (
            calculate_returns(stock_data)
        )

        # -----------------------------------
        # EQUAL WEIGHTS
        # -----------------------------------
        num_stocks = len(stocks)

        weights = np.array(
            [1 / num_stocks] * num_stocks
        )

        # -----------------------------------
        # PORTFOLIO METRICS
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
        # RANDOM PORTFOLIOS
        # -----------------------------------
        results = generate_random_portfolios(
            mean_returns,
            covariance_matrix,
            num_portfolios
        )

        # -----------------------------------
        # OPTIMIZATION
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
        # INDEXES
        # -----------------------------------
        max_sharpe_idx = np.argmax(
            results["sharpe_ratio"]
        )

        min_vol_idx = np.argmin(
            results["volatility"]
        )

        best_weights = results["weights"][
            max_sharpe_idx
        ]

        # -----------------------------------
        # KPI METRICS
        # -----------------------------------
        st.subheader("📌 Portfolio Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Expected Return",
                f"{expected_return * 252 * 100:.2f}%"
            )

        with col2:
            st.metric(
                "Portfolio Risk",
                f"{volatility * np.sqrt(252) * 100:.2f}%"
            )

        with col3:
            st.metric(
                "Sharpe Ratio",
                f"{sharpe:.2f}"
            )

        st.markdown("---")

        # -----------------------------------
        # TABS
        # -----------------------------------
        tab1, tab2, tab3 = st.tabs([
            "📈 Overview",
            "📊 Analytics",
            "⚡ Optimization"
        ])

        # ===================================
        # TAB 1 — OVERVIEW
        # ===================================
        with tab1:

            st.subheader("Portfolio Allocation")

            allocation_df = pd.DataFrame({
                "Stock": stocks,
                "Weight": best_weights
            })

            fig_pie = px.pie(
                allocation_df,
                names="Stock",
                values="Weight",
                hole=0.4
            )

            fig_pie.update_layout(
                template="plotly_dark"
            )

            st.plotly_chart(
                fig_pie,
                use_container_width=True
            )

            st.subheader("Portfolio Weights")

            st.dataframe(
                allocation_df.style.format({
                    "Weight": "{:.2%}"
                }),
                use_container_width=True
            )

        # ===================================
        # TAB 2 — ANALYTICS
        # ===================================
        with tab2:

            st.subheader("Risk vs Return")

            fig_scatter = px.scatter(
                x=results["volatility"],
                y=results["returns"],
                color=results["sharpe_ratio"],
                labels={
                    "x": "Volatility",
                    "y": "Returns",
                    "color": "Sharpe Ratio"
                }
            )

            fig_scatter.update_layout(
                template="plotly_dark"
            )

            st.plotly_chart(
                fig_scatter,
                use_container_width=True
            )

            # -----------------------------------
            # Correlation Heatmap
            # -----------------------------------
            st.subheader("Correlation Heatmap")

            corr_matrix = daily_returns.corr()

            fig_heatmap = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto",
                color_continuous_scale="RdBu"
            )

            fig_heatmap.update_layout(
                template="plotly_dark"
            )

            st.plotly_chart(
                fig_heatmap,
                use_container_width=True
            )

        # ===================================
        # TAB 3 — OPTIMIZATION
        # ===================================
        with tab3:

            st.subheader("Efficient Frontier")

            fig_frontier = go.Figure()

            fig_frontier.add_trace(
                go.Scatter(
                    x=results["volatility"],
                    y=results["returns"],
                    mode="markers",
                    marker=dict(
                        size=5,
                        color=results["sharpe_ratio"],
                        colorscale="Viridis",
                        showscale=True
                    ),
                    name="Portfolios"
                )
            )

            fig_frontier.update_layout(
                template="plotly_dark",
                xaxis_title="Volatility",
                yaxis_title="Return",
                height=700
            )

            st.plotly_chart(
                fig_frontier,
                use_container_width=True
            )

            st.subheader("Optimal Portfolio")

            optimal_df = pd.DataFrame({
                "Stock": stocks,
                "Optimal Weight": best_weights
            })

            st.dataframe(
                optimal_df.style.format({
                    "Optimal Weight": "{:.2%}"
                }),
                use_container_width=True
            )