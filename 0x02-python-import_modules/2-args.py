#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_c = len(sys.argv) - 1
    if args_c == 0:
        print("{} arguments.".format(0))
    else:
        if args_c == 1:
            print("{} argument:".format(args_c))
        else:
            print("{} arguments:".format(args_c))
        for i in range(1, args_c + 1):
            print("{}: {}".format(i, sys.argv[i]))
