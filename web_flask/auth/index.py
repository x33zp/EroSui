#!/usr/bin/python3
"""Index"""
from web_flask.auth import app_auth


@app_auth.route('/status', strict_slashes=False)
def status():
    """Returns a JSON status message"""
    return "Test Passed"
