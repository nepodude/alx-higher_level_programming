#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result_set = (i if i not in set_2 for i in set_1, j if j not in set_1 for j in set_2)
    return result_set
