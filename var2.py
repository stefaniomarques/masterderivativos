#var-2
# Historical V@R

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

assets = ['VALE3.SA', 'SUZB3.SA', 'PRIO3.SA', 'ITSA4.SA', 'BBAS3.SA', 'BBDC4.SA']
weights = np.array([0.34, 0.21, 0.19, 0.07, 0.06, 0.001])

start = '2021-10-13'
end = '2023-10-13'

portfolio = yf.download(assets, start = start, end = end)['Adj Close']
portfolio.head()

returns = portfolio.pct_change()
returns.head()
portfolioreturn = (returns * weights).sum(axis=1)
portfolioreturn.head()

# dataframe
portfolioreturndf = pd.DataFrame()
portfolioreturndf["Returns"] = portfolioreturn
portfolioreturndf.head()

# V@R
confidence_level = 0.95
historical_var = np.nanpercentile(portfolioreturndf, (1-confidence_level)*100)
print(f"Historical VaR at {confidence_level*100}% confidence level: {historical_var:.4f}")

#Plot
plt.hist(portfolioreturndf, bins=10, density=True, alpha=0.6, color='g', label='Returns')
# Add a vertical line to mark the VaR
plt.axvline(x=historical_var, color='r', linestyle='--', label=f'{confidence_level*100}% VaR')
# Add labels and legend
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.legend()
# Show the plot
plt.title('Historical Value at Risk (VaR) Calculation')
plt.show()

## Some exercises

# Calculate the total portfolio value at the end date
#total_portfolio_value = (portfolio.iloc[-1] * weights).sum()
total_portfolio_value = 1000000
var_currency = total_portfolio_value * historical_var / 100
print(f"Historical VaR at {confidence_level*100}% confidence level: ${var_currency:.2f}")

## 10-day VaR
trading_days_per_year = 252
# Scale daily returns to 10 days
scaled_returns = returns * np.sqrt(10)
# Calculate the portfolio returns for 10 days
portfolio_return_10_days = (scaled_returns * weights).sum(axis=1)
# Calculate the VaR for 10 days
historical_var_10_days = np.nanpercentile(portfolio_return_10_days, (1 - confidence_level) * 100)
# Calculate the 10-day VaR in currency amount
var_10_days_currency = total_portfolio_value * historical_var_10_days / 100
print(f"10-Day VaR at {confidence_level*100}% confidence level: ${var_10_days_currency:.2f}")

## 10-day Var at 99%
# Define the confidence level (99%)
confidence_level_10_days = 0.99
# Calculate the VaR for 10 days at a 99% confidence level
historical_var_10_days_99_percent = np.nanpercentile(portfolio_return_10_days, (1 - confidence_level_10_days) * 100)
# Calculate the 10-day VaR at 99% confidence level in currency amount
var_10_days_99_percent_currency = total_portfolio_value * historical_var_10_days_99_percent / 100
print(f"10-Day VaR at {confidence_level_10_days*100}% confidence level: ${var_10_days_99_percent_currency:.2f}")