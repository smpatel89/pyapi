#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/scoretest/<int:score>')
def pass_fail(score):
    return render_template("highscore.html", marks = score)

if __name__ == '__main__':
    app.run(port=5006, debug=True)
