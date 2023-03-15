#!/usr/bin/python3

def weight_average(my_list=[]):
    numerator_sum = 0.0
    denomenator_sum = 0.0

    if my_list is None or len(my_list) == 0 or not isinstance(my_list, list):
        return 0

    for t in my_list:
        numerator_sum = numerator_sum + (t[0] * t[1])
        denomenator_sum = denomenator_sum + t[1]

    if denomenator_sum == 0:
        return 0

    return float(numerator_sum / denomenator_sum)
