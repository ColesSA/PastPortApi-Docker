"""The ORM Class Models for the DB"""
from sqlalchemy import Column, Integer, DateTime, Float, func
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

class Location(BASE):
    """ORM Class Model for the Location object\n
    Arguments:
        BASE {DeclarativeMeta} -- Constructor Object Type.
    """

    __tablename__ = 'locations'
    def __init__(self, coords):
        self.latitude = coords['data-latitude']
        self.longitude = coords['data-longitude']

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=func.now())
    latitude = Column(Float(10))
    longitude = Column(Float(10))
