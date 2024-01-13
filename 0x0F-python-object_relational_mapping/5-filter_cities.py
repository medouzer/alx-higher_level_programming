#!/usr/bin/python3
"""
lists all cities of the state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def print_state(username, password, database, state):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    print_state(user, password, database, state_name)
