#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from os import getenv

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, default=str(uuid.uuid4()),
                             primary_key=True)
    created_at = Column(DateTime, nullable=False,
                                     default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                                     default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            datetime_keys = ['created_at', 'updated_at']
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now().isoformat()
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now().isoformat()
            if '__class__' in kwargs:
                del kwargs['__class__']

            for key, value in kwargs.items():
                if key in datetime_keys:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == '_sa_instance_state':
                    del kwargs[key]
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        attr = {k: v for k, v in self.__dict__.items() if k != '_sa_instance_state'}
        return '[{}] ({}) {}'.format(cls, self.id, attr)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key, value in dictionary.items():
            if key == '_sa_instance_state':
                del dictionary[key]
        return dictionary

    def delete(self):
        storage.delete()
