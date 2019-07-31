#!/usr/bin/python3
from flask import Flask, render_template
from got_get import get_got

app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('hellobasic.html')

#@app.route('/<username>')
@app.route('/')
def user_builder():
    got_data = get_got()
    return render_template('hellobasic2.html', data_list=got_data)

if __name__ == '__main__':
    app.run(port=5006, debug=True)
