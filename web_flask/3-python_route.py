#!/usr/bin/python3
""" Adding a variable URL and REPLACE all _ with ' ' in url end
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Base URL
    """
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """ Prints HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints C followed by the text argument
    """
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_is_magic(text="is cool"):
    """ Prints Python followed by the text argument
    If no argument, is cool is printed after by default
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
