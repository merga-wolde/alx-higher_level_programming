#!/usr/bin/python3

"""
File: 9-model_state_filter_a.py
Desc: This module contains a python script that lists all
State objects that contain the letter a from the database hbtn_0e_6_usa


"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        print("{}: {}".format(state.id, state.name))
