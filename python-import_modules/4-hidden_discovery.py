#!/usr/bin/python3
import hidden_4


def run():
    for indx in dir(hidden_4):
        if indx[:2] != "__":
            print("{}".format(indx))


if __name__ == "__main__":
    run()
