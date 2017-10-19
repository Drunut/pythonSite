# TODO: Figure out with I want to use Flask or Django
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
# TODO: Figure out how to deliver a specific web page

if __name__ == '__main__':
    app.run()