#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        display = i
        if i % 3 == 0 and i % 5 == 0:
            display = "FizzBuzz"
        elif i % 3 == 0:
            display = "Fizz"
        elif i % 5 == 0:
            display = "Buzz"
        print("{} ".format(display), end="")
