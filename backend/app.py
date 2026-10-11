
from flask import Flask, jsonify,send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Get the absolute path of the backend folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Get the data folder path
DATA_DIR = os.path.join(BASE_DIR, "data")
@app.route('/data/<filename>')
def get_csv(filename):
    allowed_files = ['matches.csv', 'deliveries.csv']

    if filename not in allowed_files:
        return jsonify({'error': 'File not found'}), 404

    return send_from_directory(DATA_DIR, filename)

@app.route('/api/batting', methods=['GET'])
def get_batting_data():

    # Read deliveries.csv using its absolute path
    deliveries_path = os.path.join(DATA_DIR, "deliveries.csv")
    df = pd.read_csv(deliveries_path)

    # Calculate total runs scored by each batter
    runs = df.groupby('batter')['batsman_runs'].sum().reset_index()

    # Count balls for each batter
    balls = df.groupby('batter')['ball'].count().reset_index()

    # Combine runs and balls
    stats = pd.merge(runs, balls, on='batter')

    # Calculate strike rate
    stats['strike_rate'] = (
        stats['batsman_runs'] / stats['ball']
    ) * 100

    # Get the top 10 batters by total runs
    top_10 = stats.sort_values(
        by='batsman_runs',
        ascending=False
    ).head(10)

    # Match the column name expected by the frontend
    top_10 = top_10.rename(
        columns={'batter': 'batsman'}
    )

    return jsonify(top_10.to_dict(orient='records'))


@app.route('/')
def home():
    return jsonify({
        "message": "IPL Analytics API is running"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
