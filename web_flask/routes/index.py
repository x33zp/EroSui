#!/usr/bin/python3
"""Index"""
from web_flask.routes import app_routes


@app_routes.route('/status', strict_slashes=False)
def status():
    """Returns a JSON status message"""
    return "Test Passed"
