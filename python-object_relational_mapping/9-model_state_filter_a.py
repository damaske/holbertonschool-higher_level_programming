#!/usr/bin/python3
""" script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (session.query(State)
                  .filter(State.name.like('%a%'))
                  .order_by(State.id)):
        print("{}: {}".format(state.id, state.name))

    if session:
        session.close()
