from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/api/batting', methods=['GET'])
def get_batting_data():
    df = pd.read_csv('data/deliveries.csv')

    # The column in your CSV is 'batter', not 'batsman'
    runs = df.groupby('batter')['batsman_runs'].sum().reset_index()
    balls = df.groupby('batter')['ball'].count().reset_index()
    stats = pd.merge(runs, balls, on='batter')
    
    stats['strike_rate'] = (stats['batsman_runs'] / stats['ball']) * 100
    
    top_10 = stats.sort_values(by='batsman_runs', ascending=False).head(10)
    
    # Rename 'batter' back to 'batsman' to match what your frontend expects
    top_10 = top_10.rename(columns={'batter': 'batsman'})

    return jsonify(top_10.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)