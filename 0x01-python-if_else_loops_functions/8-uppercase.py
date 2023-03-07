#!/usr/bin/python3

def uppercase(str):
    upper_str = ""

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        upper_str = upper_str + c
    print(upper_str)
