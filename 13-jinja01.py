#!/usr/bin/python3
import flask as Flask, render_template

app = Flask(__name__)

app.route('/')
def index():
    return render_template('hellobasic.html')

if __name__ == '__main__':
    app.run(port=5006, debug=True)
