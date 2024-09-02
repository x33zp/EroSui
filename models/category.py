#!/usr/bin/python3
"""This module creates a Category class"""
from models.base_model import BaseModel


class Category(BaseModel):
    """Class for managing category objects"""

    name = ""
    product_id = ""
    description = ""
