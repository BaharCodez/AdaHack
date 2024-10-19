from flask import Flask, render_template, request
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        user_stock_choice = request.form['stock']
        user_money_invest = float(request.form['investment'])
        startDate = request.form['start_date']
        endDate = request.form['end_date']

        # Convert startDate and endDate to datetime objects
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        endDate = datetime.strptime(endDate, '%Y-%m-%d')

        # Download data using yfinance
        data = yf.download(user_stock_choice, start=startDate, end=endDate)

        # Check if the data is empty or not available
        if data.empty:
            return render_template('result.html', error="No data found for the specified stock and date range.")

        high_values = data["High"]

        # Get the high price for the start and end dates
        start_high = high_values.asof(startDate)
        end_high = high_values.asof(endDate)

        # Check if the high values for start and end dates are available
        if pd.isna(start_high) or pd.isna(end_high):
            return render_template('result.html', error="No valid data for the selected dates.")

        # Calculate the shares bought and the value change
        shares_bought = user_money_invest / start_high
        original_value = user_money_invest
        new_value = shares_bought * end_high
        growth = (new_value / original_value - 1) * 100

        return render_template('result.html', original_value=original_value, new_value=new_value, growth=growth)

    except Exception as e:
        return render_template('result.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

