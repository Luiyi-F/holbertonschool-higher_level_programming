#!/usr/bin/python3
for alpha_letters in range(90, 64, -1):
    if alpha_letters % 2 == 0:
        alpha_letters += 32
    else:
        alpha_letters = alpha_letters
    print("{}".format(chr(alpha_letters)), end="")
