from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data

# This blueprint handles some basic routes that you can use for testing
simple_routes = Blueprint('simple_routes', __name__)


# ------------------------------------------------------------
# / is the most basic route
# Once the api container is started, in a browser, go to 
# localhost:4000/playlist
@simple_routes.route('/')
def welcome():
    current_app.logger.info('GET / handler')
    welcome_message = '<h1>Welcome to the CS 3200 Project Template REST API</h1>'
    response = make_response(welcome_message)
    response.status_code = 200
    return response

# ------------------------------------------------------------
# /playlist returns the sample playlist data contained in playlist.py
# (imported above)
@simple_routes.route('/playlist')
def get_playlist_data():
    current_app.logger.info('GET /playlist handler')
    response = make_response(jsonify(sample_playlist_data))
    response.status_code = 200
    return response

# ------------------------------------------------------------
@simple_routes.route('/niceMesage', methods = ['GET']) #Get request: methods = ['GET'] is the default, if you don't specify it it will be a GET request
def affirmation():
    message = '''
    <H1>Think about it...</H1>
    <br />
    You only need to be 1% better today than you were yesterday!
    '''
    response = make_response(message)
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Demonstrates how to redirect from one route to another. 
@simple_routes.route('/message')
def mesage():
    return redirect(url_for(affirmation))

# ------------------------------------------------------------
# This route demonstrates how to return a JSON response
# with a 200 status code. 
# general note: flask knows about these routes because we registered them with the app in rest_entry.py
#                in the __init__.py file.
@simple_routes.route('/hello')
def hello():
    message = '<H1>Hello CS3200!</H1>'  
    response = make_response(message)
    response.status_code = 200
    return response

# even though we just wrote the code it will show up on the browser because we use hot reload 
# this is a feature of Flask
# ------------------------------------------------------------
