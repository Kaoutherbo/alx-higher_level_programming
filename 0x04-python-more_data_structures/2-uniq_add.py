#!/usr/bin/python3

def uniq_add(my_list=[]):
    added = []
    sum = 0
    for i in my_list:
        if i not in added:
            sum += i
            added.append(i)
    return sum
