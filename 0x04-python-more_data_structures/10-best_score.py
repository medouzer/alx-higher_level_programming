#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = -1
    key = None
    if (a_dictionary is None):
        return key
    for k, v in a_dictionary.items():
        if v > best_score:
                best_score = v
                key = k
    return key
