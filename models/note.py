#!/usr/bin/python3
"""This module creates a Note class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Note(BaseModel, Base):
    """Class for managing user objects"""
    __tablename__ = 'notes'

    data = Column(String(10000))
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
