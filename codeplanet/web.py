#!/usr/bin/python3.6
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
app.run(debug=True)
