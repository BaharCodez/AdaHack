import yfinance as yf
import pandas as pd
msft = yf.Ticker("MSFT")  

# get historical market data
hist = msft.history(period="max")
stocks = yf.tickers(market='sp100')


dividends = []

for stock in stocks:
  data = yf.download(stock, period='1y')
  dividend_yield = data['Dividends'].sum() / data['Close'].iloc[-1]

  

ticker = "AAPL"  
start_date = input("When do you want to invest? Please enter a start date.")
end_date = input("When do you want to sell your stock roughly? Please enter an end date.")

# Retrieve stock data 
data = yf.download(ticker, start=start_date, end=end_date)




