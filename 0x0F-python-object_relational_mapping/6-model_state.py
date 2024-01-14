#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db_con = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name)
    engine = create_engine(db_con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
