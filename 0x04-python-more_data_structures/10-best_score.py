#!/usr/bin/python3
def best_score(a_dictionary):
    keeper = 0
    for i in a_dictionary.values():
        if i > keeper:
            keeper = i
    return
    (key for key in a_dictionary.keys() if a_dictionary[key] == keeper)
