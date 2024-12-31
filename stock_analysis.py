import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Get User Input
stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Step 2: Download Stock Data
try:
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    if data.empty:
        raise ValueError("No data found. Please check the stock symbol and dates.")
except Exception as e:
    print(f"Error: {e}")
    exit()

# Step 3: Data Analysis
data['MA20'] = data['Close'].rolling(window=20).mean()  # 20-day moving average
data['MA50'] = data['Close'].rolling(window=50).mean()  # 50-day moving average

# Step 4: Plot Data
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label=f"{stock_symbol} Close Price", color="blue")
plt.plot(data['MA20'], label="20-Day MA", color="orange")
plt.plot(data['MA50'], label="50-Day MA", color="green")
plt.title(f"{stock_symbol} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()
