#!/usr/bin/python3
"""This module creates a User class"""
#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel, Base
from models.note import Note
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """Class for managing user objects"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    notes = relationship("Note", backref="user") 
    #last_name = Column(String(128), nullable=True)
