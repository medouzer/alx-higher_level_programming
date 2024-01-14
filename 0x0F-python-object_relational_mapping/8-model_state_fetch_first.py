#!/usr/bin/python3
"""
First state via SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_con = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name)
    engine = create_engine(db_con, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
