#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args_c = len(sys.argv) - 1
    if args_c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ["+", "-", "*", "/"]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = sub(a, b)
        elif op == "*":
            result = mul(a, b)
        elif op == "/":
            result = div(a, b)
        print("{} {} {} = {}".format(a, op, b, result))
