
from flask import Flask, render_template, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock MVRV Data Generator
def generate_mock_data(asset, freq):
    now = datetime.utcnow()
    data = []
    points = 24 if freq == 'hourly' else 7
    for i in range(points):
        timestamp = now - timedelta(hours=i) if freq == 'hourly' else now - timedelta(days=i)
        data.append({
            'time': timestamp.strftime('%Y-%m-%d %H:%M'),
            'value': round(random.uniform(1.0, 2.5), 2)
        })
    return list(reversed(data))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/mvrv/<asset>/<freq>')
def mvrv_data(asset, freq):
    return jsonify(generate_mock_data(asset, freq))

if __name__ == '__main__':
    app.run(debug=True)
