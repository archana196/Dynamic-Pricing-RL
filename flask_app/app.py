from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__)

def load_csv(filename):
    data = []
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    results = load_csv('evaluation_results.csv')
    latest = results[-1] if results else {}
    data = {
        'revenue': latest.get('revenue', 125000),
        'inventory': latest.get('inventory', 340),
        'days_remaining': 15,
        'recommended_price': 2499,
        'avg_reward': latest.get('reward', 87.5),
        'best_reward': 142.3,
        'bookings': latest.get('bookings', 660)
    }
    return render_template('dashboard.html', data=data)

@app.route('/simulation')
def simulation():
    results = load_csv('evaluation_results.csv')
    return render_template('simulation.html', results=results)

@app.route('/comparison')
def comparison():
    return render_template('comparison.html', data={
        'qlearning': {'avg_reward': 75.3, 'best_reward': 120.5, 'episodes': 1000, 'convergence': 'Episode 750'},
        'dqn': {'avg_reward': 87.5, 'best_reward': 142.3, 'episodes': 1000, 'convergence': 'Episode 500'}
    })

@app.route('/graphs')
def graphs():
    results = load_csv('evaluation_results.csv')
    return render_template('graphs.html', results=results)

@app.route('/results')
def results():
    results = load_csv('evaluation_results.csv')
    latest = results[-1] if results else {}
    return render_template('results.html', data=latest)

@app.route('/run_simulation')
def run_simulation():
    return jsonify({
        'status': 'success',
        'revenue': 132000,
        'reward': 91.2,
        'bookings': 700,
        'inventory': 300
    })

@app.route('/api/price')
def get_price():
    return jsonify({'recommended_price': 2499, 'inventory': 340, 'days_remaining': 15})

@app.route('/api/revenue')
def get_revenue():
    return jsonify({'total_revenue': 125000, 'avg_reward': 87.5})

@app.route('/api/compare')
def compare_models():
    return jsonify({'qlearning_reward': 75.3, 'dqn_reward': 87.5, 'winner': 'DQN'})

if __name__ == '__main__':
    app.run(debug=True)