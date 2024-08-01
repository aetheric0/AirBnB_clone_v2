#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if ('HBNB_TYPE_STORAGE') is not None:
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')

    @property
    def cities(self):
        """ Returns list of city from file storage
        """
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
