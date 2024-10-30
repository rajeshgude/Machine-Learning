import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf

def load_data(stock_symbol, start_date, end_date):
    """Load stock data from Yahoo Finance."""
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data

def train_model(data):
    """Train a linear regression model."""
    data['Date'] = data.index
    data['Open'] = data['Open'].shift(-1)
    data.dropna(inplace=True)
    
    X = data[['Open', 'High', 'Low', 'Volume']].values
    y = data['Close'].values
    
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_next_day(model, last_close):
    """Predict the next day's closing price."""
    last_open = float(last_close)  # Ensure this is a float
    last_high = last_open + 1.0  # Example high value
    last_low = last_open - 1.0  # Example low value
    last_volume = 1000000.0  # Example volume, ensure it's a float

    # Create a 2D input array for the model
    next_day_price = model.predict(np.array([[last_open, last_high, last_low, last_volume]]))  # Input should be 2D
    return next_day_price[0]  # Return the predicted price
