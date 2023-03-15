#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string,str):
        return 0

    conversion_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    number_len = len(roman_string)
    roman_num = 0

    for i in range(number_len - 1, -1, -1):
        curr = roman_string[i]

        if i + 1 < number_len:
            prev = roman_string[i + 1]
        else:
            prev = None

        if curr in conversion_map:
            if prev is not None:
                if conversion_map[curr] < conversion_map[prev]:
                    roman_num = roman_num - conversion_map[curr]
                else:
                    roman_num = roman_num + conversion_map[curr]
            else:
                roman_num = roman_num + conversion_map[curr]

    return roman_num
