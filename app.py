#!/usr/bin/env python

# TODO: Figure out with I want to use Flask or Django
# So we can use render_template function, then so we can use Flask constructor
import flask

app = flask.Flask(__name__)

@app.route('/')
def homePage():
    return flask.render_template('index.html')

@app.route('/hello/<name>/')
def hello(name):
    # Displays the page greeting who ever comes to visit it.
    return flask.render_template('hello.html', name=name)

@app.route('/helloWorld')
def hello_world():
    return 'Hello, World!'
# TODO: Figure out how to deliver a specific web page

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)