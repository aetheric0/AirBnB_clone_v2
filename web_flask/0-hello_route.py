#!/usr/bin/python3
""" Module using flask to print Hello message
"""
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_world():
    """ Prints Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
