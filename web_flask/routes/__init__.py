#!/usr/bin/python3
"""Init"""
from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

from web_flask.routes.index import *
from web_flask.routes.products import *
