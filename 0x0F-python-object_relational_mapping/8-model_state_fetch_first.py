#!/usr/bin/python3
"""Prints the first State object from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                       sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
try:
    result = session.query(State).first()
    print("{}: {}".format(result.id, result.name))
except:
    print("States is empty or does not exist")
session.close()
