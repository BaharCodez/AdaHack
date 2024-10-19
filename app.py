from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_stock_choice = request.form['stock']
    user_money_invest = float(request.form['investment'])
    startDate = request.form['start_date']
    endDate = request.form['end_date']

    # Download data using yfinance
    data = yf.download(user_stock_choice, start=startDate, end=endDate)
    high_values = data["High"]

    specific_dates = [startDate, endDate]
    high_for_dates = high_values.loc[specific_dates]

    shares_bought = user_money_invest / high_for_dates[startDate]
    original_value = user_money_invest
    new_value = shares_bought * high_for_dates[endDate]
    growth = (new_value / original_value - 1) * 100

    return render_template('result.html', original_value=original_value, new_value=new_value, growth=growth)

if __name__ == '__main__':
    app.run(debug=True)

