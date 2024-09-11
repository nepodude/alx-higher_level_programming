#!/usr/bin/python3
def pow(a, b):
    answer = 1
    if b < 0:
        b = -b
        for i in range(b):
            answer *= a
        answer = 1 / answer
    else:
        for i in range(b):
            answer *= a
    return answer
