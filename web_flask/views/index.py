#!/usr/bin/python3
"""Index"""
from web_flask.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns a JSON status message"""
    return "Test Passed"
