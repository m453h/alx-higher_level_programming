#!/usr/bin/python3
"""
Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]
                            ),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
        .filter(State.name == sys.argv[4])\
        .order_by(State.id)\
        .first()

    if state is not None and sys.argv[4] == state.name:
        print("{}".format(state.id))
    else:
        print("Not found")
