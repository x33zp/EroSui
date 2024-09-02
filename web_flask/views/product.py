#!/usr/bin/python3
from web_flask.views import app_views


@app_views.route('/products/', strict_slashes=False)
def products_list():
    return "All Products"


@app_views.route('/products/<id>', strict_slashes=False)
def products_detail(id):
    return "Product ID"
