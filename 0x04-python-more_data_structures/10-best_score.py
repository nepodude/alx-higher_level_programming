#!/usr/bin/python3
def best_score(a_dictionary):
    keeper = 0
    helper = 0
    for i in a_dictionary.values():
        keeper = i
        if keeper > helper:
            helper = keeper
    return
    (key for key in a_dictionary.keys() if a_dictionary[key] == helper)