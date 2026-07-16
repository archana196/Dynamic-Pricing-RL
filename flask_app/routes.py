from flask import render_template, jsonify

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

    # API routes for RL integration
    @app.route('/api/price', methods=['GET'])
    def get_price():
        return jsonify({
            'recommended_price': 2499,
            'inventory': 340,
            'days_remaining': 15
        })

    @app.route('/api/revenue', methods=['GET'])
    def get_revenue():
        return jsonify({
            'total_revenue': 125000,
            'avg_reward': 87.5
        })