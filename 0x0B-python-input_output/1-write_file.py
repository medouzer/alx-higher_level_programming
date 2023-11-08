#!/usr/bin/python3
""" write file"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, 'w', encoding="utf-8") as f:
            f.write(text)
            return len(text)
