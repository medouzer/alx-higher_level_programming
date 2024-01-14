#!/usr/bin/python3
"""
All states Contains `a` via SQLAlchemy
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
    states = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
