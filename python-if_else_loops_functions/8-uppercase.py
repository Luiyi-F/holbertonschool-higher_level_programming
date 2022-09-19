#!/usr/bin/env python3
def uppercase(str):
    for indx in str:
        if islower(indx):
            indx = chr(ord(indx) - 32)
        print("{}".format(indx), end="")
    print("")


def islower(c):
    c = ord(c)
    if c >= 97 and c <= 122:
        return True
    else:
        return False