#!/usr/bin/python3
"""This module creates a Order class"""
from models.base_model import BaseModel


class Order(BaseModel):
    """Class for managing order objects"""

    user_id = ""
    description = ""
