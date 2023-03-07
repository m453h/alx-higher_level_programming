#!/usr/bin/python3

for i in range(90, 64, -1):
    if i % 2 == 0:
        j = 32
    else:
        j = 0
    print(chr(i + j), end='')
