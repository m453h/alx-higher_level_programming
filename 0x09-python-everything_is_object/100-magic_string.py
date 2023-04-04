#!/usr/bin/python3
def magic_string():
    n = magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool" if n == 0 else "BestSchool, " * (n - 1) + "BestSchool"
