#!/usr/bin/python3
"""Index"""
from web_flask.auth import auth


@auth.route('/status', strict_slashes=False)
def status():
    """Returns a JSON status message"""
    return "Test Passed"
