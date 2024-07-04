from config.database import base
from sqlalchemy import Column, Integer, String


class Vinyls(base):
    """
    Vinyls table of the database
    """
    __tablename__ = 'vinyls'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist = Column(String)
    label = Column(String)
    release_year = Column(String)
