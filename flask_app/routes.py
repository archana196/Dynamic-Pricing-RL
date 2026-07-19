from flask import render_template, jsonify
import random

def configure_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/dashboard')
    def dashboard():
        data = {
            'revenue': 125000,
            'inventory': 340,
            'days_remaining': 15,
            'recommended_price': 2499,
            'train_episodes': 1000,
            'avg_reward': 87.5,
            'best_reward': 142.3
        }
        return render_template('dashboard.html', data=data)

    @app.route('/results')
    def results():
        data = {
            'recommended_price': 2499,
            'inventory': 340,
            'days_remaining': 15,
            'revenue': 125000
        }
        return render_template('results.html', data=data)

    @app.route('/comparison')
    def comparison():
        data = {
            'qlearning': {
                'avg_reward': 75.3,
                'best_reward': 120.5,
                'episodes': 1000,
                'convergence': 'Episode 750'
            },
            'dqn': {
                'avg_reward': 87.5,
                'best_reward': 142.3,
                'episodes': 1000,
                'convergence': 'Episode 500'
            }
        }
        return render_template('comparison.html', data=data)

    @app.route('/api/price', methods=['GET'])
    def get_price():
        return jsonify({
            'recommended_price': 2499,
            'inventory': 340,
            'days_remaining': 15,
            'source': 'placeholder'
        })

    @app.route('/api/revenue', methods=['GET'])
    def get_revenue():
        return jsonify({
            'total_revenue': 125000,
            'avg_reward': 87.5,
            'reward_history': [45, 62, 75, 83, 87.5]
        })

    @app.route('/api/compare', methods=['GET'])
    def compare_models():
        return jsonify({
            'qlearning_reward': 75.3,
            'dqn_reward': 87.5,
            'winner': 'DQN'
        })