#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') != None:
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False, backref='place_amenities')

    """Association table for Many-to-Many relationship between Place and Amenity
    """
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

    @property
    def reviews(self):
        """ Returns list of review instances connected to a Place
        """
        from models import storage
        review_list = []
        for review in storage.all(Review).values():
            if reviews.place_id == Place.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """ Returns list of Amenity instances connected to a Place
        """
        from models import storage
        amenity_list = []
        for amenity_id in storage.all(Amenity).values():
            if Amenity.id == Place.id:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, value):
        """ Appends an amenity id to the amenity_id attribute
        """
        from models import storage
        if value.__class__.__name__ == 'Amenity':
            Amenity.id.append(value.id)
