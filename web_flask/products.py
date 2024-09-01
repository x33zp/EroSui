#!/usr/bin/python3
"""Route for Products"""
from flask import Flask

app = Flask(__name__)


@app.route('/products/', strict_slashes=False)
def products():
    return "All Products"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
