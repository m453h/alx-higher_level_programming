#!/usr/bin/python3
"""
Defines a City model which inherits from SQLAlchemy Base
City model is linked to MySQL table cities
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents the cities table in MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store cities.
        id (sqlalchemy.Integer): Represents cities table id column.
        name (sqlalchemy.String): Represents cities table name column.
        state_id (sqlalchemy.Integer): Represents cities table state_id column.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True,  nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
