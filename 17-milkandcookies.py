#!/usr/bin/python3

#!/usr/bin/env python3
from flask import Flask, make_response, request, render_template

app = Flask(__name__)

# entry point for our users
# renders a template that asks for their name
# index.html points to /setcookie
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

# set the cookie and send it back to the user
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["nm"]
        checked = request.form['box']

    # Note that cookies are set on response objects.
    # Since you normally just return strings
    # Flask will convert them into response objects for you
    resp = make_response(render_template("readcookie.html"))
    # add a cookie to our response object
                   #cookievar #value
    resp.set_cookie("userID", user)
    resp.set_cookie("checked", checked)

    # return our response object includes our cookie
    return resp

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    try:
        name = request.cookies.get("userID")
        return '<h1>welcome '+name+'</h1><p>You have not checked the box</p>'
    except:
        return render_template('auth-failed.html')


if __name__ == "__main__":
    app.run(port=5006)
