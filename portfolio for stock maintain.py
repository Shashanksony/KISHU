import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

# Fetch stock data
def get_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    return stock.history(start=start_date, end=end_date)

# Sample portfolio
portfolio = {
    'AAPL': 10,  # 10 shares of Apple
    'MSFT': 15,  # 15 shares of Microsoft
    'GOOGL': 8,  # 8 shares of Alphabet (Google)
}

start_date = '2023-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Fetch portfolio data
def fetch_portfolio_data(portfolio, start_date, end_date):
    portfolio_data = {}
    for symbol, shares in portfolio.items():
        data = get_stock_data(symbol, start_date, end_date)
        portfolio_data[symbol] = data['Close'] * shares
    return pd.DataFrame(portfolio_data)

portfolio_df = fetch_portfolio_data(portfolio, start_date, end_date)
portfolio_df['Total'] = portfolio_df.sum(axis=1)
print(portfolio_df)

# Plot portfolio
def plot_portfolio(portfolio_df):
    plt.figure(figsize=(10, 6))
    for column in portfolio_df.columns[:-1]:  # Exclude 'Total'
        plt.plot(portfolio_df.index, portfolio_df[column], label=column)
    plt.plot(portfolio_df.index, portfolio_df['Total'], label='Total', linewidth=2, linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Value ($)')
    plt.title('Portfolio Value Over Time')
    plt.legend()
    plt.show()

plot_portfolio(portfolio_df)
