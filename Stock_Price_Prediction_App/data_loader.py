import pandas as pd
import yfinance as yf

def load_data(stock_symbol, start_date, end_date):
    """Load stock data from Yahoo Finance."""
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data

def preprocess_data(data):
    """Preprocess the data for training."""
    data['Returns'] = data['Close'].pct_change()
    data['Lagged_Close'] = data['Close'].shift(1)
    data = data.dropna()  # Drop rows with NaN values

    X = data[['Lagged_Close']]  # Feature: previous day's closing price
    y = data['Close']  # Target: today's closing price
    
    return X, y
