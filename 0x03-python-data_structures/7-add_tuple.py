#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0 if len(tuple_a) < 1 else tuple_a[0]
    b = 0 if len(tuple_a) < 2 else tuple_a[1]
    c = 0 if len(tuple_b) < 1 else tuple_b[0]
    d = 0 if len(tuple_b) < 2 else tuple_b[1]

    return (a + c, b + d)
