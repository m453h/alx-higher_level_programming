#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_c = len(sys.argv) - 1
    sum = 0

    for i in range(1, args_c + 1):
        sum = sum + int(sys.argv[i])
    print("{}".format(sum))
