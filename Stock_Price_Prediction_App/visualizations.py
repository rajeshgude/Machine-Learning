import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_data(data):
    """Plot stock closing prices."""
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
