# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn-more')
def learn_more():
    return render_template('learn-more.html')

@app.route('/get-started')
def get_started():
    return render_template('get-started.html')

if __name__ == '__main__':
    app.run(debug=True)
