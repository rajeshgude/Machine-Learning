import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from model import load_data, train_model, predict_next_day

# Streamlit application title
st.title('Stock Price Prediction App')

# User input for stock ticker and date range
ticker = st.text_input('Enter Stock Ticker (e.g., AAPL)', 'AAPL')
start_date = st.date_input('Start Date', pd.to_datetime('2020-01-01'))
end_date = st.date_input('End Date', pd.to_datetime('2023-12-31'))

# Load and train the model
if st.button('Load Data and Train Model'):
    stock_data = load_data(ticker, start_date, end_date)
    st.session_state.model = train_model(stock_data)  # Store the model in session state
    st.session_state.stock_data = stock_data  # Store stock data in session state
    st.success('Model trained successfully!')

# Predicting the next day's price without user input for last closing price
if st.button('Predict Next Day Price'):
    if 'model' in st.session_state:  # Check if the model exists in session state
        # Use the last closing price from the stock data
        last_close = st.session_state.stock_data['Close'].iloc[-1]  # Get the last closing price
        next_day_price = predict_next_day(st.session_state.model, last_close)

        # Ensure next_day_price is a scalar value before formatting
        predicted_price_value = next_day_price.item()  # Convert to a scalar
        st.write(f'The predicted price for the next day is: ${predicted_price_value:.2f}')
    else:
        st.error('Please train the model first by clicking the "Load Data and Train Model" button.')

# Optional: Show the model's performance or stock data
if st.checkbox('Show Stock Data'):
    if 'stock_data' in st.session_state:  # Check if stock data exists in session state
        st.subheader('Stock Data')
        st.write(st.session_state.stock_data)

        # Plotting the stock prices
        st.subheader('Stock Price Chart')
        plt.figure(figsize=(10, 5))
        plt.plot(st.session_state.stock_data['Date'], st.session_state.stock_data['Close'], label='Close Price', color='blue')
        plt.title(f'Stock Prices for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        st.pyplot(plt)  # Display the plot in Streamlit

    else:
        st.error('Please load the stock data first by clicking the "Load Data and Train Model" button.')
