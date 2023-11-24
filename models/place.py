#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from os import getenv

typeStorage = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    if typeStorage == 'db':
        city_id = Column(String(60), nullable=False)
        user_id = Column(String(60), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer(0), nullable=False)
        number_bathrooms = Column(Integer(0), nullable=False)
        max_guest = Column(Integer(0), nullable=False)
        price_by_night = Column(Integer(0), nullable=False)
        latitude = Column(Float(), nullable=False)
        longitude = 0.0
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
