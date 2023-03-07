#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

print(f"The last digit of {number:d} is {last_digit:d} and is", end=' ')

if last_digit == 0:
    print("0")
elif last_digit > 5:
    print("greater than 5")
else:
    print("less than 6")
