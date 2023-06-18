#!/usr/bin/python3
"""
Defines a State model which inherits from SQLAlchemy Base
State model is linked to MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    Represents the states table in MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        id (sqlalchemy.Integer): Represents state table id column.
        name (sqlalchemy.String): Represents state table name column.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,  nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
