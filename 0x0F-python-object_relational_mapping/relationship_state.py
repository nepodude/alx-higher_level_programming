#!/usr/bin/python3
"""
Defines the State class with a relationship to the City class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that represents a row in the 'states' table.
    Establishes a relationship with the City class.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship: If State is deleted, all related cities are deleted
    cities = relationship("City", back_populates="state", cascade="all, delete")
