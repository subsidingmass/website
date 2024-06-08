# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

dbPath = os.path.join(os.path.dirname(__file__), 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbPath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



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
