#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for indx in matrix:
        for value in indx:
            print("{:d}".format(value), end=" ")
        print("")
