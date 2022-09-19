#!/usr/bin/python3
def run():
    for numbers1 in range(0, 9):
        for numbers2 in range(1, 10):
            if numbers1 < numbers2 :
                if numbers1 == 8 and numbers2 == 9:
                    print("{}{}".format(numbers1, numbers2))
                print("{}{}, ".format(numbers1, numbers2), end="")

if __name__ == '__main__':
    run()
