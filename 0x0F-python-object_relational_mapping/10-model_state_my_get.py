#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""
import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}?charset=utf8'.format(
                username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
