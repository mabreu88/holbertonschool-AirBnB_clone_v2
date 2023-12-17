#!/usr/bin/python3
''' Flask web application '''

from flask import Flask
from flask import render_template
from models.state import State
from models.state import City
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def teardown_appcontext(self):
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
