#!/usr/bin/python3
"""
Defines a State model which inherits from SQLAlchemy Base
State model is linked to MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
