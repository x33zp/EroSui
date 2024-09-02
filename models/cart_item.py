#!/usr/bin/python3
"""This module creates a CartItem class"""
from models.base_model import BaseModel


class CartItem(BaseModel):
    """Class for managing cart item objects"""

    cart_id = ""
    product_id = ""
    quantity = 0
