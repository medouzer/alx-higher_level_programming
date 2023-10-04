#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            newstr += chr(ord(c) - 32)
        else:
            newstr += c
    print("{}".format(newstr))
