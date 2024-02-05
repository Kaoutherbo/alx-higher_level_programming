#!/usr/bin/python3
"""
    A custom list class that inherits from
    the built-in list class.
    """


class MyList(list):
    """
sh: 1: q: not found
    in ascending sorted order
    """
    def print_sorted(self):
        print(sorted(self))
