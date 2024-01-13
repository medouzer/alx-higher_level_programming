#!/usr/bin/python3
"""
this script to list state in the arg
"""
import MySQLdb
import sys


def print_state(username, password, database, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{:s}'\
                ORDER BY id".format(state_name))
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
