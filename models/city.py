#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        String(60),
        ForeignKey('states.id'),
        nullable=False
    )

    from os import getenv
    typeStorage = getenv("HBNB_TYPE_STORAGE")

    if (typeStorage == "db"):
        places = relationship('Place', backref="cities", cascade="all, delete")