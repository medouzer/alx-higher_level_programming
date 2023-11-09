#!/usr/bin/python3
""" prints the list """


class MyList(list):
    """ function"""

    def print_sorted(self):
        print(sorted(self))
