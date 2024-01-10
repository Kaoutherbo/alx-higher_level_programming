#!/usr/bin/python3

def search_replace(my_list, search, replace):
    up_list = [i for i in my_list]
    for i in range(len(up_list)):
        if up_list[i] == search:
            up_list[i] = replace
    return up_list
