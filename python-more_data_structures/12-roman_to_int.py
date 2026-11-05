#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0
    right_value = 0

    for symbol in reversed(roman_string):
        if symbol not in values:
            return 0
        value = values[symbol]
        if value < right_value:
            total -= value
        else:
            total += value
        right_value = value

    return total
