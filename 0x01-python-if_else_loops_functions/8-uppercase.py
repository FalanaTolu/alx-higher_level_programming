#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) >= 97 and ord(str[c]) <= 122:
            lett = chr(ord(str[c]) - 32)
        else:
            lett = str[c]
            print("{:s}".format(lett), end="")
    print("")
