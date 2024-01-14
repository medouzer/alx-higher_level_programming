#!/usr/bin/python3
"""
Cities in state
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db_con = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name)
    engine = create_engine(db_con, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in all_cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
