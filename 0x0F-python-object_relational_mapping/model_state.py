#!/usr/bin/python3
"""
Defines the State class using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()


class State(Base):
    """Represents a state in the database."""
    __tablename__ = 'states'
    # Links to the MySQL table 'states'

    id = Column(
        Integer, primary_key=True, autoincrement=True,
        nullable=False, unique=True
        )
    name = Column(String(128), nullable=False)
