#!/usr/bin/python3
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    print(request.method)
    return f'Welcome\nHome {name}'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        #user = request.form['nm']   
        print(request.values)
        user = request.values.get('nm')
        print(user)
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get['nm']
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(port=5006, debug=True)
