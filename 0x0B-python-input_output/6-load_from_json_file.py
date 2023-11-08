#!/usr/bin/python3
""" load from json"""
import json


def load_from_json_file(filename):
    """ function"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
