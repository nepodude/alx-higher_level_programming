#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        character = ord(letter)
        if ord(letter) >= ord('a') and ord(letter) <= ord('a'):
             character -= 32
            print("{}".format(chr(character)), end='')
        else:
            print("{}".format(chr(character)), end='')
