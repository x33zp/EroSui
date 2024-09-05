#!/usr/bin/python3
"""Index"""
from flask import render_template
from web_flask.views import app_views


@app_views.route('/', strict_slashes=False)
def status():
    return render_template('home.html')
