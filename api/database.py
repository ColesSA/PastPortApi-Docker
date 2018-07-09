"""API Database Resources"""


import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from api.config import Config
from api.logger import time_function

engine = create_engine(Config.DB['URI'], pool_size=10, max_overflow=20)
Session = sessionmaker(bind=engine)
base = declarative_base(bind=engine)

storeSession = Session()
lastSession = Session()
allSession = Session()

@time_function
def to_database(obj):
    """Store the object into the database
    
    Arguments:
        obj {Declarative_Base} -- SqlAlchemy Base ORM object to be stored
    
    Returns:
        Declarative_base -- ORM Object stored in database
    """
    try:
        storeSession.add(obj)
        storeSession.commit()
        logging.debug('Stored to database')
        return obj
    except Exception as _x:
        storeSession.rollback()
        logging.exception('Database storage session error: %s', (_x))
        storeSession.close()
        
