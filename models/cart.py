#!/usr/bin/python3
"""This module creates a Cart class"""
from models.base_model import BaseModel


class Cart(BaseModel):
    """Class for managing cart objects"""

    user_id = ""
    total_price = ""
