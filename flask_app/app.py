from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    data = {'revenue': 125000, 'inventory': 340, 'recommended_price': 2499}
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
