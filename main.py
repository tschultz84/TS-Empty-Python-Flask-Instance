# This page contains most of the actual functions and routes. 

import flask

main = flask.Blueprint('main',__name__)


@main.route('/')
def index():

    # Initialize. 
    python_data=dict()

    # Output a string. 
    python_data['output_string'] = 'Hello world! Welcome to the empty Python Flask app.'
    
    return flask.render_template('index.html',python_data=python_data)
