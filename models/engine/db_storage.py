#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.base_model import Base

env = getenv("HBNB_ENV")
user = getenv("HBNB_MYSQL_USER")
password = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
database = getenv("HBNB_MYSQL_DB")
typeStorage = getenv("HBNB_TYPE_STORAGE")


class DBStorage():
    "Declaration of DBStorage class"
    __engine = None
    __session = None

    def __init__(self):

        from sqlalchemy import create_engine

        conn = f'mysql+mysqldb://{user}:{password}@{host}/{database}'
        self.__engine = create_engine(conn, pool_pre_ping=True)

        if (env == "test"):
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            data = self.__session.query().all()
        else:
            data = self.__session.query(cls).all()

        obj_dict = {}
        for obj in data:
            obj_dict[f'{obj.__class__.__name__}.{obj.id}'] = obj

        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)

        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False,
                               )
        from sqlalchemy.orm import scoped_session
        self.__session = scoped_session(Session)

    def close(self):
        """close session"""
        self.__session.close()
