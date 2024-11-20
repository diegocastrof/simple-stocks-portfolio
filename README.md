# Portfolio Management System

A Python-based portfolio management system that allows tracking and analysis of stock positions, including profit calculations and annualized returns.

## Features

- Track multiple stock positions in a portfolio
- Calculate portfolio value at any given date
- Compute profit/loss between two dates
- Calculate annualized returns

## Installation

1. Clone this repository:
```bash
git clone https://github.com/diegocastrof/simple-stocks-portfolio.git
cd simple-stocks-portfolio
```

## Usage

### Basic Portfolio Management

```python
from datetime import datetime
from portfolio import Portfolio, Stock

# Create a new portfolio
portfolio = Portfolio()

# Add stocks to your portfolio
portfolio.add_stock(Stock("AAPL", 100))  # 100 shares of Apple
portfolio.add_stock(Stock("GOOGL", 50))  # 50 shares of Google

# Remove a stock if needed
portfolio.remove_stock("AAPL")
```

### Calculating Profits

```python
# Define date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Calculate profit
profit = portfolio.profit(start_date, end_date)
print(f"Profit: ${profit:,.2f}")

# Calculate annualized return
annual_return = portfolio.annualized_return(start_date, end_date)
print(f"Annualized Return: {annual_return:.2f}%")
```

## Class Structure

### Stock Class
```python
Stock(symbol: str, shares: int)
- price(date: datetime) -> float  # Returns stock price at given date
```

### Portfolio Class
```python
Portfolio()
- add_stock(stock: Stock) -> None
- remove_stock(symbol: str) -> None
- value_at_date(date: datetime) -> float
- profit(start_date: datetime, end_date: datetime) -> float
- annualized_return(start_date: datetime, end_date: datetime) -> float
```

## Technical Details

### Annualized Return Formula
```
annualized_return = (1 + total_return)^(1/years) - 1

where:
- total_return = (end_value / start_value) - 1
- years = days_between_dates / 365.0
```

### Requirements
- Python 3.7+
- datetime (standard library)
- math (standard library)
- typing (standard library)

## Implementation Note
The `Stock.price()` method is not implemented. A dummy value is return instead.