#!/usr/bin/python3

def best_score(a_dictionary):
    key = None
    best = -1
    if (a_dictionary is None):
        return key
    for k, v in a_dictionary.items():
        if v > best:
            best = v
            key = k
    return key
