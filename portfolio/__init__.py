from datetime import datetime
from typing import Dict
import math

class Stock:
    def __init__(self, symbol: str, shares: int):
        self.symbol = symbol
        self.shares = shares
    
    def price(self, date: datetime) -> float:
        # This would typically fetch historical price data
        # Implementation left to be connected to actual data source
        # Return dummy value for now
        return date.day * 10.0

class Portfolio:
    def __init__(self):
        self.holdings: Dict[str, Stock] = {}
    
    def add_stock(self, stock: Stock) -> None:
        """Add a stock position to the portfolio."""
        self.holdings[stock.symbol] = stock
    
    def remove_stock(self, symbol: str) -> None:
        """Remove a stock position from the portfolio."""
        if symbol in self.holdings:
            del self.holdings[symbol]
    
    def value_at_date(self, date: datetime) -> float:
        """Calculate the total portfolio value at a given date."""
        return sum(
            stock.shares * stock.price(date)
            for stock in self.holdings.values()
        )
    
    def profit(self, start_date: datetime, end_date: datetime) -> float:
        """
        Calculate the absolute profit between two dates.
        
        Args:
            start_date: The starting date for the calculation
            end_date: The ending date for the calculation
            
        Returns:
            float: The total profit (or loss if negative)
        
        Raises:
            ValueError: If start_date is after end_date
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
            
        start_value = self.value_at_date(start_date)
        end_value = self.value_at_date(end_date)
        
        return end_value - start_value
    
    def annualized_return(self, start_date: datetime, end_date: datetime) -> float:
        """
        Calculate the annualized return between two dates.
        
        Args:
            start_date: The starting date for the calculation
            end_date: The ending date for the calculation
            
        Returns:
            float: The annualized return as a percentage
        
        Raises:
            ValueError: If start_date is after end_date or if start_value is 0
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
            
        start_value = self.value_at_date(start_date)
        
        if start_value == 0:
            raise ValueError("Initial portfolio value cannot be zero")
            
        end_value = self.value_at_date(end_date)
        
        days_between = (end_date - start_date).days
        
        if days_between == 0:
            return 0.0
        
        years = days_between / 365.0     

        total_return = (end_value / start_value) - 1       
        annualized_return = math.pow(1 + total_return, 1/years) - 1
        
        return annualized_return * 100 
    

