#!/usr/bin/python3
"""
Get a state via SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db_con = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name)
    engine = create_engine(db_con, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_search = session.query(State).\
        filter(State.name == state_name).first()
    if state_search:
        print(state_search.id)
    else:
        print("Not found")
    session.close()
