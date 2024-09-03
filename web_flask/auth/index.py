#!/usr/bin/python3
"""Index"""
from web_flask.auth import app_auth


@app_auth.route('/login', strict_slashes=False)
def login():
    return "Login"


@app_auth.route('/logout', strict_slashes=False)
def logout():
    return "Logout"


@app_auth.route('/sign-up', strict_slashes=False)
def sign_up():
    return "Sign Up"
