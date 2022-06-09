#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            str = ord(c) - 32
            print("{}".format(chr(str)), end="")
    print()
