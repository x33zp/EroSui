#!/usr/bin/python3
"""Init"""
from flask import Blueprint

app_auth = Blueprint('app_auth', __name__)

from web_flask.auth.index import *
