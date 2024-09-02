#!/usr/bin/python3
"""This module creates a OrderItem class"""
from models.base_model import BaseModel


class OrderItem(BaseModel):
    """Class for managing order item objects"""

    order_id = ""
    product_id = ""
    quantity = ""
    total_price = ""
