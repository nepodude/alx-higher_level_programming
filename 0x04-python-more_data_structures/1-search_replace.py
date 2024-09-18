#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [x if x != search for x in my_list else x = replace]
    return new_list
