#!/usr/bin/python3
"""
Defines the City class that links to the MySQL table 'cities'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base  # Import Base from relationship_state

class City(Base):
    """
    City class that represents a row in the 'cities' table.
    Establishes a relationship with the State class.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship with State
    state = relationship("State", back_populates="cities")
