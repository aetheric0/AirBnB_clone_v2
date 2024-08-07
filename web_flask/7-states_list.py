#!/usr/bin/python3
""" Routes states_list with State objects in storage
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Retrieves the states table and sorts the data in it for rendering
    """
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda st: st.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
