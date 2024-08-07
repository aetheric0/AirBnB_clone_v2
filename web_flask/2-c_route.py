#!/usr/bin/python3
""" Adding a route with a variable name
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Prints Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """ Prints HBNB
    """
    return "HBNB"


@app.route('/c/<text>/', strict_slashes=False)
def c_is_fun(text):
    """ Displays "C " followed by string in <text>
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return "C {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
