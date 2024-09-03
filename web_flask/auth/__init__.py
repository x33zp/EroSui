#!/usr/bin/python3
"""Init"""
from flask import Blueprint

auth = Blueprint('auth', __name__)`

from web_flask.views.index import *
from web_flask.views.product import *
