#!/usr/bin/python3
"""
Defines the City class that links to the MySQL table 'cities'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base  # Import Base from model_state


class City(Base):
    """
    City class that represents a row in the 'cities' table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
