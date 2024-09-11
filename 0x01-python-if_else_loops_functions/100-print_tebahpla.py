#!/usr/bin/python3
for i in range(-90, -64):
    i = -i
    if i % 2 == 0:
        i += 32
    print("{}".format(chr(i)), end='')
