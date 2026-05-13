# 📊 Portfolio Risk Analyzer

A professional finance and risk analytics project built using Python, Streamlit, NumPy, Pandas, SciPy, and Plotly.

This project helps investors analyze stock portfolios by calculating portfolio risk, expected returns, Sharpe Ratio, portfolio allocation, and efficient frontier optimization using Modern Portfolio Theory.

Designed as an internship-level finance + data analytics project, this application demonstrates practical implementation of:

* Portfolio Optimization
* Risk Management
* Financial Data Analysis
* Data Visualization
* Interactive Dashboard Development
* Quantitative Finance Concepts

---

# 🚀 Project Overview

The Portfolio Risk Analyzer is an interactive financial analytics dashboard that allows users to:

* Analyze multiple stocks together
* Calculate expected portfolio returns
* Measure portfolio volatility (risk)
* Generate thousands of random portfolios
* Find optimal portfolio allocation
* Maximize Sharpe Ratio
* Minimize portfolio risk
* Visualize the Efficient Frontier
* Explore correlation between stocks

The project fetches real-time historical stock market data and performs mathematical portfolio optimization using statistical and financial models.

---

# 🧠 Key Concepts Used

## Modern Portfolio Theory (MPT)

The project is based on Harry Markowitz’s Modern Portfolio Theory which focuses on:

* Maximizing return
* Minimizing risk
* Diversification
* Efficient asset allocation

---

## Sharpe Ratio

Used to measure risk-adjusted returns.

Formula:

Sharpe Ratio = (Portfolio Return - Risk Free Rate) / Portfolio Volatility

Higher Sharpe Ratio = Better portfolio performance.

---

## Efficient Frontier

The Efficient Frontier represents portfolios that provide:

* Maximum return for a given level of risk
* Minimum risk for a given level of return

The dashboard visualizes thousands of random portfolios to identify the optimal allocation.

---

# 🏗️ Project Architecture

```text
portfolio_risk_analyzer/
│
├── dashboard/
│   └── app.py
│
├── scripts/
│   ├── __init__.py
│   ├── data_fetcher.py
│   ├── returns_calculator.py
│   ├── risk_calculator.py
│   ├── optimizer.py
│   └── visualization.py
│
├── data/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core Programming           |
| Streamlit  | Interactive Dashboard      |
| Pandas     | Data Processing            |
| NumPy      | Numerical Computing        |
| SciPy      | Portfolio Optimization     |
| Plotly     | Interactive Visualizations |
| Matplotlib | Financial Charts           |
| yFinance   | Stock Market Data          |

---

# 📂 Module Explanation

## 1️⃣ data_fetcher.py

Responsible for fetching historical stock market data.

### Features

* Downloads stock price data
* Uses Yahoo Finance API through yFinance
* Supports multiple stock symbols
* Returns cleaned adjusted close prices

### Example

```python
fetch_stock_data(["AAPL", "MSFT", "GOOGL"])
```

---

## 2️⃣ returns_calculator.py

Calculates financial return metrics.

### Calculates

* Daily Returns
* Mean Returns
* Covariance Matrix

### Financial Importance

* Mean returns estimate future performance
* Covariance matrix measures relationship between stocks

---

## 3️⃣ risk_calculator.py

Contains core portfolio mathematics.

### Functions Included

* Portfolio Return
* Portfolio Variance
* Portfolio Volatility
* Sharpe Ratio
* Portfolio Performance

### Mathematical Concepts

* Matrix multiplication
* Statistical variance
* Annualized returns
* Risk-adjusted performance

---

## 4️⃣ optimizer.py

Handles portfolio optimization using numerical optimization.

### Features

* Generates random portfolios
* Calculates Efficient Frontier
* Maximizes Sharpe Ratio
* Minimizes Volatility
* Uses SciPy SLSQP Optimization

### Optimization Constraints

* Total weights sum to 1
* No short selling
* Asset weights between 0 and 1

---

## 5️⃣ visualization.py

Creates portfolio visualizations.

### Includes

* Efficient Frontier Graph
* Risk vs Return Plot
* Portfolio Allocation Pie Chart

---

## 6️⃣ app.py

Main Streamlit dashboard application.

### Dashboard Features

* Professional dark UI
* Sidebar portfolio settings
* KPI overview cards
* Interactive charts
* Correlation heatmap
* Efficient frontier visualization
* Portfolio allocation analysis

---

# 📈 Dashboard Features

## 📌 Portfolio Overview

Displays:

* Expected Return
* Portfolio Risk
* Sharpe Ratio

---

## 📊 Analytics Section

Includes:

* Risk vs Return Scatter Plot
* Correlation Heatmap
* Portfolio Statistics

---

## ⚡ Optimization Section

Shows:

* Efficient Frontier
* Optimal Portfolio Allocation
* Best Portfolio Weights

---

# 🔄 Project Workflow

```text
User Inputs Stock Symbols
           ↓
Fetch Historical Stock Data
           ↓
Calculate Daily Returns
           ↓
Generate Covariance Matrix
           ↓
Create Random Portfolios
           ↓
Calculate Risk & Return
           ↓
Optimize Portfolio
           ↓
Visualize Efficient Frontier
           ↓
Display Interactive Dashboard
```

---

# 📊 Financial Metrics Used

| Metric            | Purpose                       |
| ----------------- | ----------------------------- |
| Expected Return   | Measures profitability        |
| Variance          | Measures dispersion           |
| Volatility        | Measures portfolio risk       |
| Sharpe Ratio      | Measures risk-adjusted return |
| Covariance Matrix | Measures asset relationship   |

---

# 💻 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/singhdivyanshu337-cell/portfolio_risk_analyzer.git
```

---

## 2️⃣ Move Into Project Folder

```bash
cd portfolio_risk_analyzer
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Run CLI Version

```bash
python main.py
```

---

# 📸 Sample Dashboard Components

## Dashboard Contains

* Portfolio Overview Cards
* Portfolio Allocation Pie Chart
* Risk vs Return Analytics
* Correlation Heatmap
* Efficient Frontier Visualization
* Optimal Weight Distribution

---

# 📉 Example Portfolio Analysis

Example Input:

```text
AAPL, MSFT, GOOGL
```

The system:

* Downloads stock data
* Calculates returns
* Measures portfolio risk
* Finds optimal allocation
* Displays visualization dashboard

---

# 🧪 Example Optimization Logic

The optimizer generates thousands of random portfolios and compares:

* Portfolio Return
* Portfolio Volatility
* Sharpe Ratio

Then identifies:

* Best Sharpe Ratio Portfolio
* Minimum Risk Portfolio

---

# 🔐 Risk Management Features

The project helps users understand:

* Diversification benefits
* Correlation between assets
* Portfolio exposure
* Risk-adjusted performance
* Volatility analysis

---

# 🌟 Internship-Level Learning Outcomes

This project demonstrates practical skills in:

## Finance

* Portfolio Theory
* Risk Analytics
* Quantitative Finance
* Financial Modeling

## Data Analytics

* Data Cleaning
* Statistical Analysis
* Data Visualization
* Dashboard Development

## Python Development

* Modular Programming
* API Integration
* Numerical Computing
* Optimization Algorithms

---

# 🚀 Future Scope

Future improvements that can be added:

* Value at Risk (VaR)
* Monte Carlo Simulation
* Machine Learning Price Prediction
* Live Market Streaming
* Portfolio Backtesting
* Risk Forecasting
* Sentiment Analysis Integration
* Multi-Asset Portfolio Support
* Crypto Portfolio Analysis
* PDF Report Generation
* User Authentication
* Cloud Deployment

---

# 📚 Concepts Practiced

* Financial Engineering
* Portfolio Optimization
* Statistical Analysis
* Python Automation
* Streamlit Dashboard Design
* Data Visualization
* Quantitative Analysis

---

# 🎯 Project Objectives

The main objective of this project is to build a practical financial analytics system capable of:

* Evaluating portfolio performance
* Understanding market risk
* Optimizing investment allocation
* Visualizing financial analytics interactively

---

# 🏆 Skills Demonstrated

This project highlights:

* Problem Solving
* Financial Analytics
* Python Development
* Quantitative Thinking
* Data Visualization
* Dashboard Engineering
* Optimization Techniques

---

# 👨‍💻 Author

## Divyanshu Singh

Computer Science (AI) Student

### GitHub Repository

urlPortfolio Risk Analyzer Repository[https://github.com/singhdivyanshu337-cell/portfolio_risk_analyzer](https://github.com/singhdivyanshu337-cell/portfolio_risk_analyzer)

---

# ⭐ Conclusion

Portfolio Risk Analyzer is a complete finance analytics project that combines:

* Data Science
* Quantitative Finance
* Python Programming
* Dashboard Development
* Portfolio Optimization

The project provides a strong internship-level demonstration of financial analytics and risk management concepts using real-world stock market data.
