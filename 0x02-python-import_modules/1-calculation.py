#!/usr/bin/python3
from calculator_1 import *
if __name__ == "__main__":
    a = 10
    b = 5
    operations  = ["+", "-", "*", "/"]

    for op in operations:
    	if op == "+":
    		result = add(a, b)
    	elif op == "-":
    		result = sub(a, b)
    	elif op == "*":
    		result = mul(a, b)
    	elif op == "/":
    		result = div(a, b)

    	print("{} {} {} = {}".format(a, op, b, result))
