#!/usr/bin/python3
"""
Creates the State “California” with the City
'San Francisco' from the database hbtn_0e_100_usa
 """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]
                            ),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        cities = state.cities
        for city in cities:
            print("    {}: {}".format(city.id, city.name))
