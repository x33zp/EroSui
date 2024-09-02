#!/usr/bin/python3
"""This module creates a Product class"""
from models.base_model import BaseModel


class Product(BaseModel):
    """Class for managing product objects"""

    name = ""
    description = ""
    price = 0
    brand = ""
    category = ""
    in_stock = ""
