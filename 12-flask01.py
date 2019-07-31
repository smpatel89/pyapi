#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/sahil')
def n_function():
    return 'Hello Sahil'

@app.route('/hello/<name>')
def hello_name(name):
    name = name.upper()
    return f'Hello {name}'

if __name__ == '__main__':
    app.run(port=5006, debug=True)
