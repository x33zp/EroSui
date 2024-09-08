#!/usr/bin/python3
"""Init"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from web_flask.views.index import *
from web_flask.views.product import *
