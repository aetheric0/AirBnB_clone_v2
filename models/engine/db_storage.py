#!/usr/bin/python3
""" The database storage engine (MySQL)
"""
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from sqlalchemy import create_engine, text, Column
from sqlalchemy.orm import sessionmaker
import os


class DBStorage():
    __engine = None
    __session = None
    mysql_user = os.environ.get('HBNB_MYSQL_USER')
    mysql_pwd = os.environ.get('HBNB_MYSQL_PWD')
    mysql_host = os.environ.get('HBNB_MYSQL_HOST')
    mysql_db = os.environ.get('HBNB_MYSQL_DB')
    test_db = os.environ.get('HBNB_ENV')

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                self.mysql_user, self.mysql_pwd, self.mysql_host, self.mysql_db
                , pool_pre_ping=True)
        )

        if self.test_db == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all the objects in the database
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
#            objs.extend(self.__session.query(Review).all())
#            objs.extend(self.__session.query(Amenity).all())

        else:
            objs = self.__session.query(cls).all()
        return {'{}.{}'.format(type(item).__name__, item.id): item for item in objs}

    def new(self, obj):
        """ Adds a new objects to storage and saves it
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """ Saves a new object to storage
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from storage
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Loads the storage
        """
        from sqlalchemy.orm import sessionmaker

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """ Closes the session
        """
        self.__session.close()
