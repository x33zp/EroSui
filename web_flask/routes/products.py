#!/usr/bin/python3
from web_flask.routes import app_routes


@app_routes.route('/products/', strict_slashes=False)
def products_list():
    return "All Products"


@app_routes.route('/products/<id>', strict_slashes=False)
def products_detail(id):
    return "Product ID"
