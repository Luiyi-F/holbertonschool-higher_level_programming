#!/usr/bin/python3
from sys import argv


def run():
    num = 0
    for indx in argv[1:]:
        num += int(indx)
    print("{}".format(num))


if __name__ == "__main__":
    run()
