#!/usr/bin/python3
"""The manages serialization and deserialization
of instances to/from JSON file.
"""

import models
import os
# from models.place import Place
from models.user import User
from models.note import Note
# from models.amenity import Amenity
# from models.state import State
# from models.city import City
# from models.review import Review
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session



classes = {"User": User, "Note": Note}


class DBStorage:
    """Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __engine = None
    __session = None

    def __init__(self):
        """_summary_
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """_summary_
        """
        all_objects = {}

        if cls is None:
            classes_to_query = [User, Note]
        else:
            classes_to_query = [cls]

        for _class in classes_to_query:
            objs = self.__session.query(_class).all()
            for obj in objs:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                all_objects[key] = obj
        return all_objects

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        self.__session.add(obj)

    def save(self):
        """_summary_
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Purpose:
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """_summary_
        """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, identifier):
        """A method to retrieve one object"""
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)

        for value in all_cls.values():
            if '@' in identifier:
                if value.email == identifier:
                    return value
            else:
                if value.id == identifier:
                    return value

    def count(self, cls=None):
        """Count objects"""
        all_obj = self.all(cls)

        if cls in classes.values():
            all_obj = self.all(cls)
        return len(all_obj)
