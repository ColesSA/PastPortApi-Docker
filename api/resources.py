"""API Routing"""
import logging

from flask_restful import Resource, marshal_with

import api
from api.config import Config
from api.database import to_database, lastSession, allSession
from api.models import Loc_Fields, Location, Coordinate

class LocationsLast(Resource):
    """Last location stored in the database

    Returns:
        json -- last location stored in the database
    """
    @marshal_with(Loc_Fields)
    def get(self):
        """GET request
        
        Returns:
            json -- location
        """
        try:
            last_location = lastSession.query(Location).order_by(-Location.id).first()
            logging.debug('Obtained last location from database')
            return last_location
        except Exception as _x:
            logging.exception('Database last location error: %s', (_x))

class LocationsList(Resource):
    """All locations stored in the database

    Returns:
        json -- all locations stored in the database
    """
    @marshal_with(Loc_Fields)
    def get(self):
        """GET request
        
        Returns:
            json -- location list
        """
        try:
            all_locations = allSession.query(Location).all()
            logging.debug('Obtained all locations from database')
            return all_locations
        except Exception as _x:
            logging.exception('Database all locations error: %s', (_x))

class LocationNow(Resource):
    """Stores the current location into the database

    Returns:
        json -- last location stored in the database
    """
    @marshal_with(Loc_Fields)
    def get(self):
        """GET request
        
        Returns:
            json -- location
        """
        _response = api.conn.get_from(Config.WEB['URL'])
        _coordinate = Coordinate.from_request(_response)
        _location = Location.get_new(_coordinate)
        return to_database(_location)