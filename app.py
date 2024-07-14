# app.py

from flask import Flask, render_template
from bot import fetch_ohlcv, calculate_indicators, determine_entry_points

app = Flask(__name__)

# Example constants
symbol = 'ETH/USD'
timeframe = '1h'
limit = 200

# Home route
@app.route('/')
def home():
    # Fetch historical data
    historical_data = fetch_ohlcv(symbol, timeframe, limit)

    # Calculate indicators
    data_with_indicators = calculate_indicators(historical_data)

    # Determine entry points
    signals = determine_entry_points(data_with_indicators)

    # Render HTML template with signals data
    return render_template('index.html', signals=signals)

if __name__ == '__main__':
    app.run(debug=True)
