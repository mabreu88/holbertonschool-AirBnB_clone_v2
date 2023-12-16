#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(
        String(128),
        nullable=False
    )

    from os import getenv
    typeStorage = getenv("HBNB_TYPE_STORAGE")

    if (typeStorage == "db"):
        cities = relationship('City', backref="state", cascade="all, delete")

    if typeStorage != 'db':
        @property
        def cities(self):
            """ get list of City instances with state_id
                equals to the current State.id """
            list_cities = []
            all_cities = models.storage.all(City)
            for city_obj in all_cities.values():
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return list_cities
